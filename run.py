from algo_trader.logger import log
import sys
import os
import logging
from algo_trader.stocks.StockData import StockData
from algo_trader.ml_engine.StockDataPredictor import StockDataPredictor
import begin
from algo_trader.trader.Trader import Trader
from algo_trader.utils.Utils import Timer, SuppressOut
from algo_trader.decision_engine.DecisionEngine import DecisionEngine
from algo_trader.exceptions.algo_trader_exceptions import InvalidStockSymbolException, NoSymbolsGivenException
from algo_trader.constants.AlgoTraderContants import GlobalConstants as GC

logger = log.create_logger(__name__)

class AlgoTraderApplication:

    def __init__(self, 
                 plot,
                 mode,
                 analysis_info_to_file):
        self.plot = plot
        self.mode = mode
        self.decision_engine = DecisionEngine()
        self.analysis_info_to_file = analysis_info_to_file
        if self.analysis_info_to_file:
            self.file_logger = log.create_file_logger(__name__, GC.ANALYSIS_FILENAME)


    def _analyze_stock(self, stock):
        """
        Do the anaylis on a single stock and print results to stdout or a file
        """
        result = self.decision_engine.stock_analysis(stock, formatted_output=True)
        result_string = f'Results for {stock}:\n{result}'
        if self.analysis_info_to_file:
            self.file_logger.info(result_string)
        else:
            logger.info(result_string)


    def do_stock_analysis(self, symbols):
        """
        Perform just stock analysis with no trading

        Parameters:
            stock_list (list): a list of stock symbols, which can also contain filenames that contain stock symbols
        """
        for item in symbols:
            if os.path.isfile(item):
                content = open(item, 'r').readlines()
                symbol_list = [x.strip() for x in content]
                for symbol in symbol_list:
                    self._analyze_stock(symbol)
            else:
                try:
                    self._analyze_stock(item)
                except Exception as e:
                    logger.critical('An error has occured, likely an invalid stock symbol was given')
                    logger.error('Actual Error: ' + str(e))
                    raise InvalidStockSymbolException()


    def run_trade_loop(self):
        pass
                
        
# TODO: have some more cmd args
@begin.start(auto_convert=True)
def run(plot: 'whether prediction gets plotted'=False,
        mode: 'Options: [analysis, auto_trade]'=GC.MODE_ANALYSIS,
        symbols: 'A list of stock symbols or filenames for files containing stock stymbols'=[],
        analysis_info_to_file: 'send stock analysis results to a file'=False):

    algo_app = AlgoTraderApplication(
        plot=plot, 
        mode=mode, 
        analysis_info_to_file=analysis_info_to_file
    )

    if mode == GC.MODE_ANALYSIS:
        algo_app.do_stock_analysis(symbols)