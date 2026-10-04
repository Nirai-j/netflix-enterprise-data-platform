import random
import pandas as pd

from simulator.common.id_generator import IdGenerator
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config


def generate():

    cfg = load_config(
        "simulator/config/volumes.yaml"
    )

    invoices = pd.read_parquet(
        "simulator/output/payment/invoices.parquet"
    )

    payment_gen = IdGenerator("PAY")

    success_rate = cfg[
        "payment_success_rate"
    ]

    methods = [
        "CREDIT_CARD",
        "DEBIT_CARD",
        "PAYPAL",
        "UPI",
        "APPLE_PAY"
    ]

    rows = []

    for _, invoice in invoices.iterrows():

        success = (
            random.random()
            <= success_rate
        )

        rows.append(
            {
                "payment_id":
                    payment_gen.next_id(),

                "invoice_id":
                    invoice["invoice_id"],

                "payment_date":
                    invoice["invoice_date"],

                "payment_amount":
                    invoice["amount_due"],

                "payment_method":
                    random.choice(methods),

                "payment_status":
                    "SUCCESS"
                    if success
                    else "FAILED"
            }
        )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/payment/payments.parquet"
    )

    return df


if __name__ == "__main__":
    generate()