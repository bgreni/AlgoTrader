import pandas as pd
import matplotlib.pyplot as plt
from algo_trader.exceptions.algo_trader_exceptions import NoEnvException
import colorlog
from fbprophet import Prophet
from algo_trader.logger import log
from datetime import datetime

logger = log.create_logger(__name__)

class StockDataPredictor:

    def __init__(self):
        self.model = Prophet()

    def learn(self, data: pd.DataFrame):
        """
        Learn from stock data

        Parameters:
            data (pandas df): pandas df with the fields 'date' and  'close'
        """
        logger.debug('Learning stuff')

        # reformat data so Prophet will be happy
        data = data.reset_index(level=0)
        learn_set = data[['date', 'close']].copy()
        learn_set.rename(columns={
            'date': 'ds',
            'close': 'y'
        }, inplace=True)
        self.model.fit(learn_set)
        

    def predict(self, days=365, plot=False) -> pd.DataFrame:
        """
        Predict daily stock values for a given period in the future

        Parameters:
            days (int): days into the future we are predicting
            plot (bool): if true shows a plot of predicted values

        Returns:
            prediction (pandas df): df of 
        """
        future = self.model.make_future_dataframe(periods=days)
        prediction = self.model.predict(future)

        if plot:
            fig = self.model.plot(prediction)
            plt.show()

        return prediction[prediction['ds'] > datetime.now()]

    