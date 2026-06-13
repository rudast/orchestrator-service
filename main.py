import asyncio
import logging

from app.bot.settings import startup
from app.utils.logging import setup_logging

if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger("main")

    try:
        asyncio.run(startup())
    except KeyboardInterrupt:
        logger.info("Application stopped")
