from algo_trader.stocks.StockData import StockData
from iexfinance.apidata import get_api_status
import pytest
from mockito import when, mock, unstub, ANY
import pandas as pd
from datetime import datetime
import iexfinance

# lulz tests

# @pytest.fixture
# def stockData():
#     return StockData('', '', '')

# def test_get_stock(stockData):
#     stock = mock(iexfinance.stocks.Stock)
#     when(iexfinance.stocks).Stock(...).thenReturn(stock)
#     # when(stockData).get_stock(ANY(str)).thenReturn(stock)

#     returnStock = stockData.get_stock('AAPL')

#     assert returnStock == stock

#     unstub()

# def test_get_historical_data(stockData):
#     df = mock(pd.DataFrame)
#     when(stockData).get_historical_data(...).thenReturn(df)

    # returnDf = 