import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramConflictError, TelegramNetworkError
from aiogram.utils.token import TokenValidationError
from pydantic import ValidationError

from app.bot.handlers.start import router as start_router
from app.bot.handlers.task import router as task_router
from app.config.base import get_config

logger = logging.getLogger(__name__)


async def startup() -> None:
    bot = None
    session = None

    dispatcher = Dispatcher()

    try:
        config = get_config()

        logger.debug(f"Telegram proxy enabled: {bool(config.telegram.proxy_url)}")
        if config.telegram.proxy_url:
            session = AiohttpSession(
                proxy=config.telegram.proxy_url.unicode_string()
            )
            logger.info(f"Telegram proxy: {config.telegram.proxy_url.unicode_string()}")


        logger.info('Starting up telegram bot')

        bot = Bot(
            token=config.telegram.token.get_secret_value(),
            session=session,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML
            ),
        )

        await bot.get_me()
        logger.debug(f"Including routers")
        dispatcher.include_routers(start_router, task_router)

        await dispatcher.start_polling(bot)

    except TokenValidationError:
        logger.critical("Invalid telegram bot token")

    except TelegramConflictError:
        logger.critical("Another telegram bot is already running")

    except TelegramNetworkError:
        logger.exception("Telegram network error during bot startup")

    except ValidationError:
        logger.critical("Invalid application configuration")

    except Exception as e:
        logger.exception(f"Unhandled exception during bot startup: {e}")

    finally:
        logger.info('Closing bot connection')

        if bot and bot.session:
            await bot.session.close()
