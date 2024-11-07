import logging
from typing import Callable

pl = logging.getLogger("pybites_logger")

DEBUG = pl.debug
INFO = pl.info
WARNING = pl.warning
ERROR = pl.error
CRITICAL = pl.critical


def log_it(level: Callable, msg: str) -> None:
    return level(msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
