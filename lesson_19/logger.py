import logging

LOG_FILE = "hb_test.log"


def get_logger():
    logger = logging.getLogger("heartbeat_logger")
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger