import pandas as pd
from .connection import engine


def load():

    invoices = pd.read_parquet(
        "simulator/output/payment/invoices.parquet"
    )

    invoices.to_sql(
        "invoices",
        engine,
        schema="netflix",
        if_exists="append",
        index=False
    )

    print("Invoices Loaded")