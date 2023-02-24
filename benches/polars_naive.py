import polars as pl


def price():
    df = pl.read_csv("price.csv", try_parse_dates=True)
    agg = (
        df.select("price", "date")
        .sort("date")
        .groupby_dynamic("date", every="1y")
        .agg(pl.col("price").mean())
    )
    return agg


def n_sold():
    df = pl.read_csv("price.csv", try_parse_dates=True)
    agg = (
        df.select("date")
        .sort("date")
        .groupby_dynamic("date", every="1y")
        .agg(pl.count())
    )
    return agg


def most_expensive():
    df = pl.read_csv("price.csv", try_parse_dates=True)
    agg = (
        df.filter(pl.col("date").dt.year() >= 2020)
        .select("town", "district", "price")
        .groupby("town", "district")
        .agg(pl.count(), pl.col("price").mean())
        .filter(pl.col("count") >= 100)
        .sort("price", descending=True)
        .limit(10)
    )
    return agg
