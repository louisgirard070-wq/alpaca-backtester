import pandas as pd

from data import get_data
from indicators import add_indicators
from strategies import trend_following, mean_reversion, custom_strategy
from backtest import run_backtest
from performance import calculate_metrics
from charts import plot_price, plot_equity, plot_drawdowns


ticker = input("Enter ticker: ").upper()

df = get_data(ticker)
df = add_indicators(df)

strategies = {
    "Trend Following": trend_following,
    "Mean Reversion": mean_reversion,
    "Custom Strategy": custom_strategy
}

results = {}
metrics = {}

for name, strategy_func in strategies.items():
    strategy_df = strategy_func(df)
    backtested = run_backtest(strategy_df)

    results[name] = backtested
    metrics[name] = calculate_metrics(backtested)

    plot_price(backtested, ticker, name.replace(" ", "_").lower())

# Add Buy & Hold comparison
buy_hold = df.copy()
buy_hold["position"] = 1
buy_hold = run_backtest(buy_hold)
buy_hold["equity"] = buy_hold["buy_hold"]

results["Buy & Hold"] = buy_hold
metrics["Buy & Hold"] = calculate_metrics(buy_hold)

plot_equity(results)
plot_drawdowns(results)

metrics_df = pd.DataFrame(metrics).T

# Convert decimal values to percentages
for col in [
    "Total Return",
    "CAGR",
    "Volatility",
    "Max Drawdown",
    "Win Rate",
]:
    metrics_df[col] *= 100

# Round numbers
metrics_df = metrics_df.round(2)

# Add percent signs
metrics_df["Total Return"] = metrics_df["Total Return"].map("{:.2f}%".format)
metrics_df["CAGR"] = metrics_df["CAGR"].map("{:.2f}%".format)
metrics_df["Volatility"] = metrics_df["Volatility"].map("{:.2f}%".format)
metrics_df["Max Drawdown"] = metrics_df["Max Drawdown"].map("{:.2f}%".format)
metrics_df["Win Rate"] = metrics_df["Win Rate"].map("{:.2f}%".format)

print(metrics_df)

metrics_df.to_csv("performance_table.csv", index=True)