from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from app.config.base import config
from handlers.start import router


async def startup():
    bot = Bot(
        token=config.telegram.token.get_secret_value(),
        session=AiohttpSession(proxy=config.telegram.proxy_url.unicode_string()),
    )
    # TODO handle TokenValidationError
    # TODO add parser mode

    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    # TODO check start polling params
    await dispatcher.start_polling(bot)
