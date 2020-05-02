from iexfinance.stocks import Stock, get_historical_data
from datetime import datetime, timedelta
import os
from iexfinance.altdata import get_social_sentiment
from dotenv import load_dotenv
from algo_trader.constants.AlgoTraderContants import StockDataConstants as SC
import colorlog
import numpy as np
import pandas as pd
from algo_trader.logger import log
import pathlib
from algo_trader.exceptions.algo_trader_exceptions import NoEnvException, NoAPIVersionException, StockDataNotBuiltException
from iexfinance.data_apis import get_data_points

logger = log.create_logger(__name__)


class StockData:

    def __init__(self, key=None, sandbox_key=None, api_version=None):
        
        # try and load from .env
        has_env = load_dotenv()
        # check if creds have been passed as args
        if  key == None or sandbox_key == None and api_version == None:
            # no credentials are present at all
            if not has_env:
                logger.critical('You have no .env file to read IEX info from')
                raise NoEnvException()
            # creds exist in .env
            else:
                IEX_API_VERSION = os.getenv('IEX_API_VERSION')

                os.environ['IEX_API_VERSION'] = IEX_API_VERSION

                if IEX_API_VERSION == SC.IEX_API_VERSION_SANDBOX:
                    os.environ['IEX_TOKEN'] = os.getenv('IEX_SANDBOX_KEY')
                else:
                    os.environ['IEX_TOKEN'] = os.getenv('IEX_KEY')
        # get creds from args
        else:
            if api_version == None:
                logger.critical('No api version has been given')
                raise NoAPIVersionException('No api version has been given')
            os.environ['IEX_API_VERSION'] = api_version
            if api_version == SC.IEX_API_VERSION_SANDBOX:
                os.environ['IEX_TOKEN'] = sandbox_key
            else:
                os.environ['IEX_TOKEN'] = key

        self.pre_built = False

    
    def build(self, stock):
        """
        Preload all important metrics to avoid making multiple api calls for the same information

        Parameters:
            stock (str): ticker string of the stock
        """
        self.stock = Stock(stock)
        
        self.quote = self.stock.get_quote()
        self.pe_ratio = self.quote[SC.PE_RATIO]
        self.price_to_book = get_data_points(stock, SC.PRICE_TO_BOOK)
        self.debt_to_equity = get_data_points(stock, SC.DEBT_TO_EQUITY)
        self.peg = get_data_points(stock, SC.PEG)
        self.beta = get_data_points(stock, SC.BETA)
        self.cash_flow = get_data_points(stock, SC.CASH_FLOW)
        self.price_to_sales = get_data_points(stock, SC.PRICE_TO_SALES)
        self.payout_ratio = get_data_points(stock, SC.TTMDIVIENDS) / get_data_points(stock, SC.TTMEPS)

        self.pre_built = True


    def get_stock(self, stock) -> Stock:
        """
        Gets Stock object for the given stock

        Parameters:
            stock (str): ticker string of the stock

        Returns:
            Stock: Stock object for the given stock
        """
        return Stock(stock)

    # TODO: I'm not entirely sure if this is correct
    def get_payout_ratio(self, stock=None) -> float:
        """
        Get payout ration of a given stock

        Parameters:
            stock (str): ticker string of the stock

        Returns:
            (float): dividends payout to earnings of the stock
        """
        if self.pre_built:
            return self.payout_ratio

        self._check_args(stock)
        
        dividends_per_share = get_data_points(stock, SC.TTMDIVIENDS)
        eps = get_data_points(stock, SC.TTMEPS)

        return dividends_per_share / eps


    def get_price_to_sales(self, stock=None) -> float:
        """
        Get price to sales ratio of a given stock

        Parameters:
            stock (str): ticker string of the stock

        Returns:
            (float): price to sales of the stock
        """
        if self.pre_built:
            return self.price_to_sales

        self._check_args(stock)
        
        return get_data_points(stock, SC.PRICE_TO_SALES)


    def get_cash_flow(self, stock=None) -> int:
        """
        Get cash flow for a stock
        
        Parameters:
            stock (str): ticker string of the stock

        Returns:
            (int): the cash flow of the stock
        """
        if self.pre_built:
            return self.cash_flow

        self._check_args(stock)

        return get_data_points(stock, SC.CASH_FLOW)


    def get_beta(self, stock=None) -> float:
        """
        Get the beta value of a given stock
        Refers to the volatility of a stock
        beta > 1: more volatile
        beta < 1: less volatile

        Parameters:
            stock (str): ticker string of the stock

        Returns:
            (float): the beta value of the stock
        """
        if self.pre_built:
            return self.beta

        self._check_args(stock)

        return get_data_points(stock, SC.BETA)
            

    def get_debt_to_equity(self, stock=None) -> float:
        """
        Get the debt to equity ratio of a given stock

        Parameters:
            stock (str): ticker string of the stock

        Returns:
            (float): the total liabilities of the stock divided by shareholder equity
        """
        if self.pre_built:
            return self.debt_to_equity

        self._check_args(stock)

        return get_data_points(stock, SC.DEBT_TO_EQUITY)


    def get_price_to_earnings(self, stock=None) -> float:
        """
        Get the price to earnings ratio of a given stock

        Parameters:
            stock (str): ticker string of the stock

        Returns:
            (float): the price of the stock divided by the earnings per share of the stock
        """
        if self.pre_built:
            return self.pe_ratio

        self._check_args(stock)

        return Stock(stock).get_quote()[SC.PE_RATIO]


    def get_price_to_book(self, stock=None) -> float:
        """
        Get the price to book value ratio of a given stock

        Parameters:
            stock (str): ticker string of the stock

        Returns:
            (float): the price of the stock divided by the book value per share of the stock
        """
        if self.pre_built:
            return self.price_to_book

        self._check_args(stock)

        return get_data_points(stock, SC.PRICE_TO_BOOK)


    def get_stock_historical_data(self, stock, start, end, use_local_data=False) -> pd.DataFrame:
        """
        Get historical stock data for a given stock over a given time period

        Parameters:
            stock (str): ticker string of the stock
            start (datetime): start date for the time interval
            end (datetime): end date for the time interval
            use_local_data (bool): Use historical data stored in local file

        Returns:
            pd.DataFrame: dataframe with past stock data
        """

        if use_local_data:
            file_path = str(pathlib.Path(__file__).parent.absolute()) + '/historical_data_cache/' + stock + '.csv'
            return self._update_local_historical_data(stock, file_path)

        return get_historical_data(stock, start, end, output_format='pandas')

    """
    Helpers
    """

    def _update_local_historical_data(self, stock, file_path):
        """
        creates or updates a local version of historical stock data as a CSV file
        """
        end = datetime.now()

        if not os.path.exists(file_path):
            # create file for pandas to write to
            open(file_path, 'w').close()
            start = end - timedelta(days=5 * 365)
            df = get_historical_data(stock, start, end, output_format='pandas')
            df.to_csv(file_path)
            return df
        else:
            df = pd.read_csv(file_path)
            # get the date of the latest day we have saved
            start = pd.to_datetime(df['date']).max()
            # make our start date the next day for the api call
            # for fresh data
            start = start + timedelta(days=1)

            data = get_historical_data(stock, start, end, output_format='pandas')
            merged = pd.concat([df, data])

            merged.to_csv(file_path)

            return merged


    def _check_args(self, *args):
        if None in args:
            error_string = 'You haven\'t built stock data or passed in a stock symbol'
            logger.critical(error_string)
            raise StockDataNotBuiltException(error_string)

