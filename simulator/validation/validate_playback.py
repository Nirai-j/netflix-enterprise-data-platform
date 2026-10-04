import pandas as pd

from simulator.validation.common import (
    check_duplicates,
    check_foreign_key
)


def run():

    subscriptions = pd.read_parquet(
        "simulator/output/subscription/subscriptions.parquet"
    )

    invoices = pd.read_parquet(
        "simulator/output/payment/invoices.parquet"
    )

    payments = pd.read_parquet(
        "simulator/output/payment/payments.parquet"
    )

    accounts = pd.read_parquet(
        "simulator/output/account/accounts.parquet"
    )

    check_duplicates(
        subscriptions,
        "subscription_id"
    )

    check_duplicates(
        invoices,
        "invoice_id"
    )

    check_duplicates(
        payments,
        "payment_id"
    )

    check_foreign_key(
        subscriptions,
        accounts,
        "account_id",
        "account_id"
    )

    check_foreign_key(
        invoices,
        subscriptions,
        "subscription_id",
        "subscription_id"
    )

    check_foreign_key(
        payments,
        invoices,
        "invoice_id",
        "invoice_id"
    )

    print(
        "Revenue Validation Completed"
    )