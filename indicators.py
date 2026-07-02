import numpy as np
import pandas as pd


def add_indicators(df):
    df = df.copy()

    # SMA and EMA
    df["SMA_50"] = df["Close"].rolling(50).mean()
    df["SMA_200"] = df["Close"].rolling(200).mean()
    df["EMA_12"] = df["Close"].ewm(span=12, adjust=False).mean()
    df["EMA_26"] = df["Close"].ewm(span=26, adjust=False).mean()

    # MACD
    df["MACD"] = df["EMA_12"] - df["EMA_26"]
    df["MACD_signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

    # RSI
    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    df["RSI"] = 100 - (100 / (1 + rs))

    # Bollinger Bands
    df["BB_middle"] = df["Close"].rolling(20).mean()
    df["BB_std"] = df["Close"].rolling(20).std()
    df["BB_upper"] = df["BB_middle"] + 2 * df["BB_std"]
    df["BB_lower"] = df["BB_middle"] - 2 * df["BB_std"]

    # ATR
    high_low = df["High"] - df["Low"]
    high_close = abs(df["High"] - df["Close"].shift())
    low_close = abs(df["Low"] - df["Close"].shift())

    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    df["ATR"] = true_range.rolling(14).mean()

    # OBV
    df["OBV"] = (np.sign(df["Close"].diff()) * df["Volume"]).fillna(0).cumsum()

    # ADX simplified
    plus_dm = df["High"].diff()
    minus_dm = -df["Low"].diff()

    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm < 0] = 0

    tr = true_range
    plus_di = 100 * (plus_dm.rolling(14).mean() / tr.rolling(14).mean())
    minus_di = 100 * (minus_dm.rolling(14).mean() / tr.rolling(14).mean())

    dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
    df["ADX"] = dx.rolling(14).mean()

    return df.dropna()