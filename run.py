from algo_trader.logger import log
import sys
import logging
logger = log.create_logger(__name__)
from algo_trader.stocks.StockData import StockData
from algo_trader.ml_engine.StockDataPredictor import StockDataPredictor
from datetime import datetime
import begin

# TODO: have some more cmd args
@begin.start(auto_convert=True)
def run(plot: 'whether prediction gets plotted'=False):
    stockData = StockData()

    stock = stockData.get_stock('AAPL')

    start = datetime(2015, 1, 1)
    end = datetime.now()

    data = stockData.get_stock_historical_data('AAPL', start, end)
    
    predictor = StockDataPredictor()
    predictor.learn(data)
    prediction = predictor.predict(plot=plot)
    logger.debug(prediction)