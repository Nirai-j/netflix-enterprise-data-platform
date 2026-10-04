import pandas as pd

from simulator.common.id_generator import IdGenerator
from simulator.common.date_utils import random_date
from simulator.common.faker_utils import (
    country,
    acquisition_channel
)
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config


def generate():

    cfg = load_config(
        "simulator/config/volumes.yaml"
    )

    account_count = cfg["accounts"]

    account_gen = IdGenerator("ACC")

    rows = []

    for _ in range(account_count):

        rows.append(
            {
                "account_id": account_gen.next_id(),
                "country": country(),
                "signup_date": random_date(),
                "acquisition_channel": acquisition_channel(),
                "status": "ACTIVE"
            }
        )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/account/accounts.parquet"
    )

    return df


if __name__ == "__main__":
    generate()