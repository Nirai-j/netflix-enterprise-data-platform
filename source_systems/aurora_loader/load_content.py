import pandas as pd
from .connection import engine


def load():

    for table in [
        "titles",
        "seasons",
        "episodes"
    ]:

        df = pd.read_parquet(
            f"simulator/output/content/{table}.parquet"
        )

        df.to_sql(
            table,
            engine,
            schema="netflix",
            if_exists="append",
            index=False
        )

    print("Content Loaded")