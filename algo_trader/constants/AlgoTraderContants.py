from aenum import Constant

class GlobalConstants(Constant):
    ANALYSIS_FILENAME = 'stock_analysis.txt'
    MODE_ANALYSIS = 'analysis'
    MODE_AUTO_TRADE = 'auto_trade'

class DecisionEngineConstants(Constant):
    MAX_PAYOUT_RATIO_SCORE = 100
    OPTIMAL_PAYOUT_RATIO = 0.4
    PAYOUT_RATIO_BOUND = 0.3

    MAXIMUM_TOTAL_SCORE = MAX_PAYOUT_RATIO_SCORE

    SIG_DIGS = 2


class MLEngineConstants(Constant):
    pass


class StockDataConstants(Constant):

    IEX_API_VERSION_SANDBOX = 'iexcloud-sandbox'
    ACTUAL_EPS = 'actualEPS'
    PRICE_TO_BOOK = 'PRICETOBOOK'
    DEBT_TO_EQUITY = 'DEBTTOEQUITY'
    PEG = 'PEGRATIO'
    PE_RATIO = 'peRatio'
    BETA = 'BETA'
    CASH_FLOW = 'CASHFLOW'
    PRICE_TO_SALES = 'PRICETOSALES'
    LAST_DIVIDEND_AMOUNT ='LAST-DIVIDEND-AMOUNT'
    NET_INCOME = 'NETINCOME'
    TTMEPS = 'TTMEPS'
    TTMDIVIENDS = 'TTMDIVIDENDRATE'


class TraderConstants(Constant):
    ORDER_CLASS_SIMPLE = 'simple'
    BUY_ORDER = 'buy'
    ORDER_MARKET = 'market'
    TIME_IN_FORCE_DAY = 'day'
    ORDER_CLASS_BRACKET = 'bracket'
    TAKE_PROFIT = 'take_profit'
    STOP_LOSS = 'stop_loss'