import asyncio
import logging

from pydantic import ValidationError

from app.bot.settings import startup
from app.config.base import get_config
from app.utils.logging import setup_logging

if __name__ == "__main__":
    config = get_config()
    setup_logging(config.debug)
    logger = logging.getLogger("main")

    logger.info(f"Debug mode {"enabled" if config.debug else "disabled"}")

    try:
        logger.info("Starting application")
        asyncio.run(startup())

    except ValidationError:
        logger.error("Validation error")

    except KeyboardInterrupt:
        logger.info("Application stopped")
