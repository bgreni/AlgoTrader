import alpaca_trade_api as tradeapi
from algo_trader.logger import log
from dotenv import load_dotenv
from iexfinance.stocks import Stock
from algo_trader.exceptions.algo_trader_exceptions import NoEnvException
from algo_trader.constants.TraderConstants import TraderConstants as TC
logger = log.create_logger(__name__)

class Trader:

    def __init__(self):

        if not load_dotenv():
            raise NoEnvException('You have no .env file to read alpaca info from')

        self.api = tradeapi.REST(api_version='v2')
        # not sure if theres any actual use for doing this
        # self.account = self.api.get_account()
    
    def buy(self, stock: str, 
            qty: str='1', 
            bracket_order_info: dict=None, 
            order_class: str=TC.ORDER_CLASS_SIMPLE) -> tradeapi.entity.Order:
            
        if order_class == TC.ORDER_CLASS_SIMPLE:
            return self.api.submit_order(
                symbol=stock,
                side=TC.BUY_ORDER,
                qty=qty,
                type=TC.ORDER_MARKET,
                time_in_force=TC.TIME_IN_FORCE_DAY,
                order_class=order_class
            )
