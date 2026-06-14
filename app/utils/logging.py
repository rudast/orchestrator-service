import logging
import sys


class CenterFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        original = record.levelname
        record.levelname = f"{original:^8}"

        try:
            return super().format(record)
        finally:
            record.levelname = original


def setup_logging(debug: bool = False) -> None:
    formatter = CenterFormatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        handlers=[
            console_handler,
        ],
    )
