# ML_Engine

## Classes

### StockDataPredictor

Uses the [fbprophet](https://facebook.github.io/prophet/) machine learning forecasting library to make predictions on stock prices

#### Example use

```
# instantiate a predictor object
predictor = StockDataPredictor()

# train the model
predictor.learn(data)

# make prediction
prediction = predictor.predict()

# if you want to generate a plot of prediction
prediction = predictor.predict(plot=True)
```

#### Data expected format
`StockDataPredictor.learn()` expects data to have two columns `date` and `close` to learn from