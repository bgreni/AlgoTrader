import matplotlib.pyplot as plt
from pprint import pprint
from iexfinance.stocks import Stock, get_historical_data
from mindsdb import Predictor
from datetime import datetime
import os
from iexfinance.altdata import get_social_sentiment

if __name__ == "__main__":

    key = 'sk_092aa28ea977410980a54021efc7dd64'
    sandbox_key = 'Tsk_18ac784d016e4403bc62fc056d5960e3'

    os.environ['IEX_TOKEN'] = sandbox_key
    os.environ['IEX_API_VERSION'] = 'iexcloud-sandbox'

    stock = Stock('AAPL')
    print(stock.get_quote())

    print(get_social_sentiment("AAPL"))
    


    # key = "8PJT0AUD0Q0CHA95"

    # ts = TimeSeries(key=key, output_format="pandas")

    # data, mdata = ts.get_daily_adjusted(symbol="BTC", outputsize="full")


    # data = data.reset_index(level=0)

    # data["ds"] = data["date"]
    # data["y"] = data["5. adjusted close"]

    # # print(data.head())

    # p = Prophet()
    # p.fit(data)

    # future = p.make_future_dataframe(periods=365)

    # prediction = p.predict(future)

    # filter = prediction["ds"] >= "2010-01-01"
    # prediction = prediction[filter]
    # print("MIN DATE:", prediction["ds"].head(1))
    # print("MAX DATE:", prediction["ds"].tail(1))

    # # plot = p.plot(prediction)
    # plot = p.plot_components(prediction)
    # plt.show()