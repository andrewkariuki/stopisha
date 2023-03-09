import logging


def custom_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.WARNING)

    # File handler
    fh = logging.FileHandler(f"logs/{logger_name}.log")
    fh.setLevel(logging.INFO)

    # Stream handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # create formatter and add it to the handlers
    fmt = "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
