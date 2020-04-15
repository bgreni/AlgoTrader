from iexfinance.stocks import Stock, get_historical_data
from datetime import datetime
import os
from iexfinance.altdata import get_social_sentiment
from dotenv import load_dotenv
from .constants import StockDataConstants
import colorlog
import numpy as np
import pandas as pd
from algo_trader.logger import log
from algo_trader.exceptions.algo_trader_exceptions import NoEnvException

logger = log.create_logger(__name__)


class StockData:

    def __init__(self):
        
        if not load_dotenv():
            raise NoEnvException('You have no .env file to read IEX info from')

        IEX_API_VERSION = os.getenv('IEX_API_VERSION')

        os.environ['IEX_API_VERSION'] = IEX_API_VERSION

        if IEX_API_VERSION == StockDataConstants.IEX_API_VERSION_SANDBOX:
            os.environ['IEX_TOKEN'] = os.getenv('IEX_SANDBOX_KEY')
        else:
            os.environ['IEX_TOKEN'] = os.getenv('IEX_KEY')

    def get_stock(self, stock: str) -> Stock:
        """
        Returns Stock object for the given stock

        Parameters:
            stock (str): ticker string of the stock

        Returns
            Stock: Stock object for the given stock
        """
        return Stock(stock, output_format='pandas')
    
    def get_stock_historical_data(self, stock: str, start: datetime, end: datetime) -> pd.DataFrame:
        """
        Get historical stock data for a given stock over a given time period

        Parameters:
            stock (str): ticker string of the stock
            start (datetime): start date for the time interval
            end (datetime): end date for the time interval

        Returns:
            pd.DataFrame: dataframe with past stock data

        """
        logger.debug('getting data')
        return get_historical_data(stock, start, end, output_format='pandas')