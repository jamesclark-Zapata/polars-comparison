import pandas as pd


def price():
    df = pd.read_csv("price.csv", parse_dates=[2])
    group = df["date"].dt.to_period("Y")
    agg = df[["price", "date"]].groupby(group).price.agg("mean")
    return agg


def n_sold():
    df = pd.read_csv("price.csv", parse_dates=[2])
    group = df["date"].dt.to_period("Y")
    agg = df["date"].groupby(group).count()
    return agg


def most_expensive():
    df = pd.read_csv("price.csv", parse_dates=[2])
    agg = (
        df.query("date>=2020")
        .groupby(["town", "district"])
        .price.agg(["count", "mean"])
        .query("count>=100")
        .sort_values("mean", ascending=False)
        .iloc[:10]
    )
    return agg
