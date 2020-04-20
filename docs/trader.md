# Trader

## Classes

### Trader

A wrapper for the [alpaca_trade_api](https://github.com/alpacahq/alpaca-trade-api-python)

The following is expected to be in a .env file in `algo_trader/trader`:

- APCA_API_KEY_ID: You alpaca API key 
- APCA_API_SECRET_KEY: Your alpaca secret key
- APCA_API_BASE_URL: options are `api.alpaca.markets` for live trading or `paper-api.alpaca.markets` for paper trading
- API_VERSION

#### Usage

A simple buy order can be done as follows
```
trader = Trader()
trader.buy('AAPL')
```