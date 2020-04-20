# Stocks

## Classes

### StockData

A simple wrapper for the [iexfinance](https://pypi.org/project/iexfinance/) library. The purpose of writing this wrapper is mostly for hiding config setup and other interface simplifications. 

The following things are expected to be in a .env file in the stocks folder:
- IEX_KEY: secret obtained by creating an account at https://iexcloud.io
- IEX_SANDBOX_KEY: secret key for if you wish to use IEX sandbox mode also obtained by creating and account
- IEX_API_VERSION: the IEX api version you want to use or `iexcloud-sandbox` if you wish to use sandbox mode

The above parameters can also be passed to the StockData constructor

#### Usage

##### Getting an iexfinance Stock object

If you just want to get an IEX [Stock](https://addisonlynch.github.io/iexfinance/devel/stocks.html#the-stock-object) object, you can do so with `get_stock()` and do all the fun stuff you can do with that.
```
stockData = StockData()
stock = stockData.get_stock('AAPL')
```

##### Getting Historical Data

If you want to get past data for a stock you can use `get_stock_historical_data()`
```
stockData = StockData()
stock = 'AAPL'
start = datetime(2017, 1, 1)
end = datetime.now()
data = stockData.get_stock_historical_data(stock, start, end)
# fun stuff...
```

##### Other Methods

The other methods in StockData can be used in two different ways

You can pass a stock symbol directly into the method like so
```
beta = stockData.get_beta('AAPL)
```

Or you can prebuilt all the important data that you will likely need
```
stockData.build('AAPL)
beta = stockData.get_beta()
```

Note that any args will be ignore you have built data available.
Using `build()` will be much fast if you know you will need access to all or most of the available data more than once, since it saves on api calls. But will be much more expensive if you only wanted to use 1 or 2 data points.
