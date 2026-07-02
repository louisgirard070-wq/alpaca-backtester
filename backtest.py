def run_backtest(df, initial_capital=100000):
    df = df.copy()

    df["market_return"] = df["Close"].pct_change()
    df["strategy_return"] = df["position"].shift(1) * df["market_return"]

    df["equity"] = initial_capital * (1 + df["strategy_return"]).cumprod()
    df["buy_hold"] = initial_capital * (1 + df["market_return"]).cumprod()

    df["trade"] = df["position"].diff().fillna(0)

    return df.dropna()