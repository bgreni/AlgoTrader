from algo_trader.logger import log
import sys
import logging
logger = log.create_logger(__name__)
from algo_trader.stocks.StockData import StockData
from algo_trader.ml_engine.StockDataPredictor import StockDataPredictor
from datetime import datetime
import begin
from algo_trader.trader.Trader import Trader
from algo_trader.utils.Utils import Timer

# TODO: have some more cmd args
@begin.start(auto_convert=True)
def run(plot: 'whether prediction gets plotted'=False):

    # trader = Trader()

    # trader.buy('AAPL')

    stockData = StockData()

    stock = 'AAPL'
    stockData.build(stock)
    logger.info(stockData.get_cash_flow())
    # logger.info(stockData.get_price_to_book())
    # logger.info(stockData.get_price_to_earnings())
    # logger.info(stockData.get_debt_to_equity())

    # start = datetime(2015, 1, 1)
    # end = datetime.now()

    # data = stockData.get_stock_historical_data('AAPL', start, end)
    # logger.info(data)
    
    # predictor = StockDataPredictor()
    # predictor.learn(data)
    # prediction = predictor.predict(plot=plot)
    # logger.debug(prediction)