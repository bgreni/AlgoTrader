from algo_trader.stocks import StockData
from algo_trader.ml_engine import StockDataPredictor


class DecisionEngine:
    """
    Hopefully this is where the magic will happen
    """

    def __init__(self):
        self.stockData = StockData()
        self.predictor = StockDataPredictor()

    def should_buy_stock(self, stock):
        pass
