from algo_trader.stocks.StockData import StockData
from algo_trader.ml_engine.StockDataPredictor import StockDataPredictor
from collections import namedtuple
from algo_trader.constants.AlgoTraderContants import DecisionEngineConstants as DC
from math import e
import numpy as np
from algo_trader.logger import log
from algo_trader.utils.Utils import scale_value_distance_from_optimal

buy_info = namedtuple('buy_info', 'should_buy score predicted_earnings')
logger = log.create_logger(__name__)

class DecisionEngine:
    """
    Hopefully this is where the magic will happen
    """

    def __init__(self):
        self.stockData = StockData()
        self.predictor = StockDataPredictor()


    def stock_analysis(self, stock, hold=False, hold_duration=None, formatted_output=False):
        """
        evaluates a stock and decides whether it is worth buying

        Parameters:
            stock (str): the ticker symbol of the stock
            hold (bool): Whether the stock to be investigated will be a long term hold
            hold_duration (datetime): The maximum date in the future that should be used for hold strategy earnings predictions

        Return:
            buy_info (namedtuple): named tuple containing the following field:
                should_buy (bool): whether the stock is worth buying
                score (float): an estimated score representing the strength of the stock
                predicted_earning (float): predicted earnings from buying the stock
        """
        self.stockData.build(stock)

        total_score = 0

        payout_ratio_score = self._evaluate_payout_ratio()

        total_score += payout_ratio_score

        if formatted_output:
            output = (
                f'total score: {round(total_score, DC.SIG_DIGS)} / {DC.MAXIMUM_TOTAL_SCORE}\n'
                f'payout ratio score: {round(payout_ratio_score, DC.SIG_DIGS)} / {DC.MAX_PAYOUT_RATIO_SCORE} given for a value of {round(self.stockData.get_payout_ratio(), DC.SIG_DIGS)}\n'
            )
            return output
        
        info = buy_info(score=total_score, should_buy=False, predicted_earnings=None)
        return info

    
    def _evaluate_payout_ratio(self):
        """
        Evaluate the score of the payout ratio of the stock

        Returns:
            score (float): The scaled score
        """
        ratio = self.stockData.get_payout_ratio()
        score = DC.MAX_PAYOUT_RATIO_SCORE
        score *= scale_value_distance_from_optimal(ratio, DC.OPTIMAL_PAYOUT_RATIO, DC.PAYOUT_RATIO_BOUND)

        return score


    def _get_predicted_earnings(self, duration=365):
        """
        Get an estimate of your predicted total earnings from holding a stock for a given duration

        Parameters:
            duration (int): time to hold the stock in days
        """
        pass

