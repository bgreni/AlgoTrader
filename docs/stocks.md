# Stocks

## Classes

### StockData

A simple wrapper for the [iexfinance](https://pypi.org/project/iexfinance/) library. The purpose of writing this wrapper is mostly for hiding config setup and other interface simplifications. 

The following things are expected to be in a .env file in the stocks folder:
- IEX_KEY: secret obtained by creating an account at https://iexcloud.io
- IEX_SANDBOX_KEY: secret key for if you wish to use IEX sandbox mode also obtained by creating and account
- IEX_API_VERSION: the IEX api version you want to use or `iexcloud-sandbox` if you wish to use sandbox mode