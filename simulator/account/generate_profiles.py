import random
import pandas as pd

from simulator.common.id_generator import IdGenerator
from simulator.common.faker_utils import language
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config


def generate():

    cfg = load_config(
        "simulator/config/volumes.yaml"
    )

    accounts = pd.read_parquet(
        "simulator/output/account/accounts.parquet"
    )

    profile_gen = IdGenerator("PRO")

    rows = []

    min_profiles = cfg["profiles_per_account"]["min"]
    max_profiles = cfg["profiles_per_account"]["max"]

    for _, account in accounts.iterrows():

        profile_count = random.randint(
            min_profiles,
            max_profiles
        )

        for idx in range(profile_count):

            rows.append(
                {
                    "profile_id": profile_gen.next_id(),
                    "account_id": account["account_id"],
                    "profile_type":
                        "ADULT"
                        if idx == 0
                        else random.choice(
                            [
                                "ADULT",
                                "KIDS"
                            ]
                        ),
                    "language": language(),
                    "created_date":
                        account["signup_date"]
                }
            )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/account/profiles.parquet"
    )

    return df


if __name__ == "__main__":
    generate()