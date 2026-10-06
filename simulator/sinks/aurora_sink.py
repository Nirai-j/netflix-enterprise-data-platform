import pandas as pd

from source_systems.database.connection import get_engine


TABLES = [
    (
        "simulator/output/account/accounts.parquet",
        "account",
        "account",
    ),
    (
        "simulator/output/account/profiles.parquet",
        "account",
        "profile",
    ),
    (
        "simulator/output/subscription/plans.parquet",
        "subscription",
        "plan",
    ),
    (
        "simulator/output/subscription/subscriptions.parquet",
        "subscription",
        "subscription",
    ),
    (
        "simulator/output/payment/invoices.parquet",
        "payment",
        "invoice",
    ),
    (
        "simulator/output/payment/payments.parquet",
        "payment",
        "payment",
    ),
    (
        "simulator/output/content/titles.parquet",
        "content",
        "title",
    ),
    (
        "simulator/output/content/seasons.parquet",
        "content",
        "season",
    ),
    (
        "simulator/output/content/episodes.parquet",
        "content",
        "episode",
    ),
]


def load():
    engine = get_engine()

    for path, schema, table in TABLES:

        print(
            f"Loading {path} "
            f"→ {schema}.{table}"
        )

        df = pd.read_parquet(path)

        df.to_sql(
            name=table,
            con=engine,
            schema=schema,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=1000,
        )

    print("Aurora/PostgreSQL load completed.")


if __name__ == "__main__":
    load()