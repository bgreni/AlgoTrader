# Some stuff to better tell you how you fucked up

class NoEnvException(Exception):
    pass

class NoAPIVersionException(Exception):
    pass

class DataNotSetException(Exception):
    pass

class InvalidOrderClassException(Exception):
    pass

class StockDataNotBuiltException(Exception):
    pass

class InvalidStockSymbolException(Exception):
    pass

class NoSymbolsGivenException(Exception):
    pass