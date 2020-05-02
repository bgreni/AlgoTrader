import colorlog
import sys
from logging import FileHandler

def get_base_logger(name):
    logger = colorlog.getLogger(name)
    logger.setLevel(colorlog.colorlog.logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    # seems this prevents some logs from being logged twice
    logger.propagate = False

    return logger

def create_logger(name):
    logger = get_base_logger(name)

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(fmt='%(log_color)s%(asctime)s - %(levelname)s:%(module)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
    logger.addHandler(handler)

    return logger

def create_file_logger(name, filename):
    logger = get_base_logger(name + 'file')

    handler = FileHandler(filename, mode='w')
    handler.setFormatter(colorlog.ColoredFormatter(fmt='%(log_color)s%(asctime)s - %(levelname)s:%(module)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
    logger.addHandler(handler)

    return logger

    
