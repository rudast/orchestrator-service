import asyncio
import logging
import sys

from app.bot.settings import startup

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(startup())
