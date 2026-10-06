import pandas as pd

from .connection import engine


def load():

    accounts = pd.read_parquet(
        "simulator/output/account/accounts.parquet"
    )

    profiles = pd.read_parquet(
        "simulator/output/account/profiles.parquet"
    )

    accounts.to_sql(
        "accounts",
        engine,
        schema="netflix",
        if_exists="append",
        index=False
    )

    profiles.to_sql(
        "profiles",
        engine,
        schema="netflix",
        if_exists="append",
        index=False
    )

    print("Accounts Loaded")