import random
import pandas as pd

from simulator.common.id_generator import IdGenerator
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config


def generate():

    cfg = load_config(
        "simulator/config/volumes.yaml"
    )

    accounts = pd.read_parquet(
        "simulator/output/account/accounts.parquet"
    )

    plans = pd.read_parquet(
        "simulator/output/subscription/plans.parquet"
    )

    penetration_rate = cfg["subscriptions"][
        "penetration_rate"
    ]

    subscription_gen = IdGenerator("SUB")

    rows = []

    subscribed_accounts = accounts.sample(
        frac=penetration_rate,
        random_state=42
    )

    statuses = [
        "ACTIVE",
        "ACTIVE",
        "ACTIVE",
        "ACTIVE",
        "PAUSED",
        "CANCELLED"
    ]

    for _, account in subscribed_accounts.iterrows():

        plan = plans.sample(1).iloc[0]

        rows.append(
            {
                "subscription_id":
                    subscription_gen.next_id(),

                "account_id":
                    account["account_id"],

                "plan_id":
                    plan["plan_id"],

                "start_date":
                    account["signup_date"],

                "end_date":
                    None,

                "status":
                    random.choice(statuses)
            }
        )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/subscription/subscriptions.parquet"
    )

    return df


if __name__ == "__main__":
    generate()