import numpy as np


def calculate_metrics(df):
    returns = df["strategy_return"]
    equity = df["equity"]

    total_return = equity.iloc[-1] / equity.iloc[0] - 1

    years = len(df) / 252
    cagr = (equity.iloc[-1] / equity.iloc[0]) ** (1 / years) - 1

    volatility = returns.std() * np.sqrt(252)

    sharpe = (returns.mean() * 252) / volatility if volatility != 0 else 0

    downside_returns = returns[returns < 0]
    downside_vol = downside_returns.std() * np.sqrt(252)
    sortino = (returns.mean() * 252) / downside_vol if downside_vol != 0 else 0

    running_max = equity.cummax()
    drawdown = equity / running_max - 1
    max_drawdown = drawdown.min()

    entries = df[df["trade"] == 1].index
    exits = df[df["trade"] == -1].index
    wins = 0
    total_trades = 0
    num_trades = min(len(entries), len(exits))

    for i in range(num_trades):
        entry_price = df.loc[entries[i], "Close"]
        exit_price = df.loc[exits[i], "Close"]
        trade_return = (exit_price - entry_price) / entry_price
        if trade_return > 0:
            wins += 1
        total_trades += 1
    win_rate = wins / total_trades if total_trades > 0 else 0

    return {
        "Total Return": total_return,
        "CAGR": cagr,
        "Volatility": volatility,
        "Sharpe": sharpe,
        "Sortino": sortino,
        "Max Drawdown": max_drawdown,
        "Win Rate": win_rate,
        "Trades": total_trades
    }