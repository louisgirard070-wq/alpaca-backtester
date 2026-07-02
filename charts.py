import matplotlib.pyplot as plt
import os


def plot_price(df, ticker, name):
    os.makedirs("charts", exist_ok=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close")
    plt.plot(df.index, df["SMA_50"], label="SMA 50")
    plt.plot(df.index, df["SMA_200"], label="SMA 200")

    buys = df[df["trade"] == 1]
    sells = df[df["trade"] == -1]

    plt.scatter(
        buys.index,
        buys["Close"],
        marker="^",
        s=80,
        color="green",
        edgecolors="black",
        label="Buy"
    )

    plt.scatter(
        sells.index,
        sells["Close"],
        marker="v",
        s=80,
        color="red",
        edgecolors="black",
        label="Sell"
    )

    plt.title(f"{ticker} Price Chart - {name}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"charts/{name}_price.png")
    plt.grid(alpha=0.3)
    plt.show()


def plot_equity(results):
    plt.figure(figsize=(12, 6))

    for name, df in results.items():
        plt.plot(df.index, df["equity"], label=name)

    plt.title("Equity Curve Comparison")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.tight_layout()
    plt.savefig("charts/equity_curve.png")
    plt.grid(alpha=0.3)
    plt.show()


def plot_drawdowns(results):
    plt.figure(figsize=(12, 6))

    for name, df in results.items():
        drawdown = df["equity"] / df["equity"].cummax() - 1
        plt.plot(df.index, drawdown, label=name)

    plt.title("Drawdown Comparison")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.legend()
    plt.tight_layout()
    plt.savefig("charts/drawdowns.png")
    plt.grid(alpha=0.3)
    plt.show()