import polars as pl


def price():
    df = pl.scan_csv("price.csv", try_parse_dates=True)
    agg = (
        df.select("price", "date")
        .sort("date")
        .groupby_dynamic("date", every="1y")
        .agg(pl.col("price").mean())
    ).collect()
    return agg


def n_sold():
    df = pl.scan_csv("price.csv", try_parse_dates=True)
    agg = (
        df.select("date")
        .sort("date")
        .groupby_dynamic("date", every="1y")
        .agg(pl.count())
    ).collect()
    return agg


def most_expensive():
    df = pl.scan_csv("price.csv", try_parse_dates=True)
    agg = (
        df.filter(pl.col("date").dt.year() >= 2020)
        .select("town", "district", "price")
        .groupby("town", "district")
        .agg(pl.count(), pl.col("price").mean())
        .filter(pl.col("count") >= 100)
        .sort("price", descending=True)
        .limit(10)
    ).collect()
    return agg
