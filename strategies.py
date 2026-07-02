def trend_following(df):
    df = df.copy()
    position = 0
    positions = []

    for _, row in df.iterrows():
        buy = row["MACD"] > row["MACD_signal"] and row["ADX"] > 25
        sell = row["MACD"] < row["MACD_signal"]

        if buy:
            position = 1
        elif sell:
            position = 0

        positions.append(position)

    df["position"] = positions
    return df


def mean_reversion(df):
    df = df.copy()
    position = 0
    positions = []

    for _, row in df.iterrows():
        buy = row["RSI"] < 35 and row["Close"] < row["BB_lower"]
        sell = row["RSI"] > 65 and row["Close"] > row["BB_upper"]

        if buy:
            position = 1
        elif sell:
            position = 0

        positions.append(position)

    df["position"] = positions
    return df


def custom_strategy(df):
    df = df.copy()
    position = 0
    positions = []

    df["OBV_20"] = df["OBV"].rolling(20).mean()

    for _, row in df.iterrows():

        buy = (
            row["Close"] < row["SMA_200"] - 4 * row["ATR"]
            and row["RSI"] < 40
            and row["OBV"] > row["OBV_20"]
        )

        sell = (
            row["Close"] > row["SMA_200"] + 5 * row["ATR"]
            and row["RSI"] > 70
            and row["MACD"] < row["MACD_signal"]
        )

        if buy:
            position = 1
        elif sell:
            position = 0

        positions.append(position)

    df["position"] = positions
    return df