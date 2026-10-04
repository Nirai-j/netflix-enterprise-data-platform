import pandas as pd

from datetime import timedelta

from simulator.common.id_generator import IdGenerator
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config


def generate():

    cfg = load_config(
        "simulator/config/volumes.yaml"
    )

    subscriptions = pd.read_parquet(
        "simulator/output/subscription/subscriptions.parquet"
    )

    plans = pd.read_parquet(
        "simulator/output/subscription/plans.parquet"
    )

    invoice_gen = IdGenerator("INV")

    invoice_cycles = cfg[
        "invoices_per_subscription"
    ]

    rows = []

    for _, sub in subscriptions.iterrows():

        plan = plans[
            plans["plan_id"] ==
            sub["plan_id"]
        ].iloc[0]

        start_date = pd.to_datetime(
            sub["start_date"]
        )

        for month in range(invoice_cycles):

            invoice_date = (
                start_date +
                timedelta(days=30 * month)
            )

            rows.append(
                {
                    "invoice_id":
                        invoice_gen.next_id(),

                    "subscription_id":
                        sub["subscription_id"],

                    "account_id":
                        sub["account_id"],

                    "invoice_date":
                        invoice_date,

                    "amount_due":
                        plan["monthly_price"],

                    "invoice_status":
                        "PAID"
                }
            )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/payment/invoices.parquet"
    )

    return df


if __name__ == "__main__":
    generate()