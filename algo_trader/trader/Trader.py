import alpaca_trade_api as tradeapi
from algo_trader.logger import log
from dotenv import load_dotenv
from iexfinance.stocks import Stock
from algo_trader.exceptions.algo_trader_exceptions import NoEnvException, InvalidOrderClassException
from algo_trader.constants.AlgoTraderContants import TraderConstants as TC
logger = log.create_logger(__name__)

class Trader:

    def __init__(self):

        if not load_dotenv():
            raise NoEnvException('You have no .env file to read alpaca info from')

        self.api = tradeapi.REST(api_version='v2')
        # not sure if theres any actual use for doing this
        # self.account = self.api.get_account()
    
    def buy(self, stock, qty, bracket_order_info, 
            order_class=TC.ORDER_CLASS_SIMPLE) -> tradeapi.entity.Order:
        """
        buy a given stock
        Parameters:
            stock (str): the symbol of the stock to buy
            qty (str): number of stocks to buy as a string
            bracket_order_info (dict): information needed to make a bracket order
                see "take_profit" and "stop_loss" here 
                https://alpaca.markets/docs/trading-on-alpaca/orders/#bracket-orders
            order_class (str): the type of order being made
                options:
                    TC.ORDER_CLASS_SIMPLE
        """
            
        if order_class == TC.ORDER_CLASS_SIMPLE:
            return self.api.submit_order(
                symbol=stock,
                side=TC.BUY_ORDER,
                qty=qty,
                type=TC.ORDER_MARKET,
                time_in_force=TC.TIME_IN_FORCE_DAY,
                order_class=order_class
            )
        elif order_class == TC.ORDER_CLASS_BRACKET:
            return self.api.submit_order(
                symbol=stock,
                side=TC.BUY_ORDER,
                qty=qty,
                type=TC.ORDER_MARKET,
                time_in_force=TC.TIME_IN_FORCE_DAY,
                order_class=order_class,
                take_profit=bracket_order_info[TC.TAKE_PROFIT],
                stop_loss=bracket_order_info[TC.STOP_LOSS]
            )
        else:
            raise InvalidOrderClassException('Order class: ' + order_class + ' is not supported')
