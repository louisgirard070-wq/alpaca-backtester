import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame


def get_data(ticker):
    load_dotenv()

    api_key = os.getenv("ALPACA_API_KEY")
    secret_key = os.getenv("ALPACA_SECRET_KEY")

    client = StockHistoricalDataClient(api_key, secret_key)

    end = datetime.now()
    start = end - timedelta(days=365 * 6)

    request = StockBarsRequest(
        symbol_or_symbols=ticker,
        timeframe=TimeFrame.Day,
        start=start,
        end=end
    )

    bars = client.get_stock_bars(request)
    df = bars.df

    if isinstance(df.index, tuple) or "symbol" in df.index.names:
        df = df.loc[ticker]

    df = df.rename(columns={
        "open": "Open",
        "high": "High",
        "low": "Low",
        "close": "Close",
        "volume": "Volume"
    })

    return df