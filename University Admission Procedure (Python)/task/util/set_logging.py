import logging
import sys


def init_debug_and_info_handlers(logger):
    logger.setLevel(logging.INFO)  # Change between INFO and DEBUG

    # Create a stream handler for info messages
    info_handler = logging.StreamHandler(sys.stdout)
    info_handler.setLevel(logging.INFO)
    info_formatter = logging.Formatter('%(message)s')
    info_handler.setFormatter(info_formatter)

    # Create a stream handler for debug messages
    debug_handler = logging.StreamHandler(sys.stdout)
    debug_handler.setLevel(logging.DEBUG)
    debug_formatter = logging.Formatter('DEBUG - %(filename)s:%(lineno)d - %(message)s')
    debug_handler.setFormatter(debug_formatter)

    # Set the info handler to only handle INFO messages
    info_handler.addFilter(lambda record: record.levelno == logging.INFO)

    # Set the debug handler to only handle DEBUG messages
    debug_handler.addFilter(lambda record: record.levelno == logging.DEBUG)

    # Remove existing handlers from the logger preventing duplicate logs
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Add the handlers to the logger
    logger.addHandler(info_handler)
    logger.addHandler(debug_handler)
