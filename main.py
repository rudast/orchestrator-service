import asyncio

from app.bot.settings import startup
from app.utils.logging import setup_logging

if __name__ == "__main__":
    setup_logging()
    try:
        asyncio.run(startup())
    except KeyboardInterrupt:
        pass
