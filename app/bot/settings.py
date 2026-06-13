import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramConflictError, TelegramNetworkError
from aiogram.utils.token import TokenValidationError

from app.bot.handlers.start import router
from app.config.base import config

logger = logging.getLogger(__name__)


async def startup() -> None:
    session = None
    if config.telegram.proxy_url:
        session = AiohttpSession(
            proxy=config.telegram.proxy_url.unicode_string()
        )

    bot = Bot(
        token=config.telegram.token.get_secret_value(),
        session=session,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        ),
    )

    dispatcher = Dispatcher()

    try:
        logger.info('Starting up telegram bot')

        await bot.get_me()
        dispatcher.include_router(router)

        await dispatcher.start_polling(bot)

    except TokenValidationError:
        logger.critical("Invalid telegram bot token")

    except TelegramConflictError:
        logger.critical("Another telegram bot is already running")

    except TelegramNetworkError:
        logger.exception("Unhandled exception during bot startup")

    except Exception as e:
        logger.critical(e)

    finally:
        logger.info('Closing bot connection')

        if bot.session:
            await bot.session.close()
