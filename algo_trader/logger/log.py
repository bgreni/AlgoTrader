import colorlog

def create_logger(name):
    logger = colorlog.getLogger(name)
    logger.setLevel(colorlog.colorlog.logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    # seems this prevents some logs from being logged twice
    logger.propagate = False

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(fmt='%(log_color)s%(asctime)s - %(levelname)s:%(module)s - %(message)s', datefmt='%Y-%m-%d %H:%M'))
    logger.addHandler(handler)

    return logger
    
