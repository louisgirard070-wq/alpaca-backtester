# Alpaca Technical Indicator Backtester

A Python-based algorithmic trading backtester built using the Alpaca Historical Market Data API. The program downloads historical stock data, calculates multiple technical indicators, backtests several trading strategies, and compares their performance using common financial metrics.

## Project Demo

▶️ **Click below to watch the project demonstration**

[demo.mp4](demo.mp4)

---

## Final Report

[Final_Report.pdf](Final_Report.pdf)

---

## Features

- Downloads 6 years of daily OHLCV data from Alpaca
- User selects any supported stock ticker
- Calculates multiple technical indicators
- Backtests three algorithmic trading strategies
- Compares performance against Buy & Hold
- Computes common risk and return metrics
- Generates price, equity curve, and drawdown charts

---

## Technical Indicators

This project implements the following indicators:

- Simple Moving Average (SMA 50 & SMA 200)
- Exponential Moving Average (EMA 12 & EMA 26)
- MACD
- Relative Strength Index (RSI)
- Bollinger Bands
- Average True Range (ATR)
- On-Balance Volume (OBV)
- Average Directional Index (ADX)

---

## Trading Strategies

### Buy & Hold

Purchases the selected stock at the beginning of the testing period and holds it until the end.

---

### Trend Following

**Entry**

- MACD crosses above its signal line
- ADX > 25 (strong trend)

**Exit**

- MACD crosses below its signal line

---

### Mean Reversion

**Entry**

- RSI < 35
- Price closes below the lower Bollinger Band

**Exit**

- RSI > 65
- Price closes above the upper Bollinger Band

---

### Custom Strategy

This strategy combines indicators from four different categories:

- **Trend:** 200-day SMA
- **Momentum:** RSI and MACD
- **Volatility:** ATR
- **Volume:** OBV

**Entry**

Buy when:

- Price is at least 4 ATR below the 200-day SMA
- RSI < 40 (oversold)
- OBV is above its 20-day moving average, indicating improving buying pressure

**Exit**

Sell when:

- Price is at least 5 ATR above the 200-day SMA
- RSI > 70 (overbought)
- MACD crosses below its signal line

This strategy attempts to identify high-quality oversold buying opportunities while waiting for confirmation from both momentum and volume before entering a trade.

---

## Performance Metrics

Each strategy reports:

- Total Return
- CAGR
- Annualized Volatility
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Win Rate
- Number of Trades

---

## Charts Generated

The program automatically creates:

- Price chart with buy/sell signals
- Equity curve comparison
- Drawdown comparison

All figures are saved in the `charts/` directory.

---

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

or on Windows:

```bash
py -m pip install -r requirements.txt
```

---

## Running the Program

```bash
py main.py
```

Enter a ticker symbol when prompted, for example:

```
AAPL
```

or

```
SPY
```

---

## Technologies Used

- Python
- Alpaca Market Data API
- Pandas
- NumPy
- Matplotlib
- python-dotenv

---

## Example Output

The program produces:

- Strategy performance comparison table
- Buy & Hold benchmark
- Price charts with buy/sell signals
- Equity curve comparison
- Drawdown comparison

---

## Future Improvements

Possible extensions include:

- Transaction costs and commissions
- Stop-loss and take-profit rules
- Position sizing and portfolio optimization
- Additional technical indicators
- Parameter optimization