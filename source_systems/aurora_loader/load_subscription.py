import pandas as pd
from .connection import engine


def load():

    for table in [
        "plans",
        "subscriptions"
    ]:

        folder = (
            "subscription"
            if table in ["plans", "subscriptions"]
            else "account"
        )

        df = pd.read_parquet(
            f"simulator/output/{folder}/{table}.parquet"
        )

        df.to_sql(
            table,
            engine,
            schema="netflix",
            if_exists="append",
            index=False
        )

    print("Subscription Loaded")