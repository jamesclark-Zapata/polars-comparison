import pandas as pd


def price():
    df = pd.read_csv(
        "price.csv", parse_dates=[1], usecols=["price", "date"], index_col="date"
    )
    group = df.index.to_period("Y")
    agg = df["price"].groupby(group).agg("mean")
    return agg


def n_sold():
    df = pd.read_csv(
        "price.csv", parse_dates=[1], usecols=["date", "price"], index_col="date"
    )
    group = df.index.to_period("Y")
    agg = df["price"].groupby(group).count()
    return agg


def most_expensive():
    df = pd.read_csv(
        "price.csv",
        parse_dates=[1],
        usecols=["date", "price", "town", "district"],
        index_col="date",
    )
    agg = (
        df.loc["2020":]
        .groupby(["town", "district"])
        .price.agg(["count", "mean"])
        .query("count>=100")
        .sort_values("mean", ascending=False)
        .iloc[:10]
    )
    return agg
