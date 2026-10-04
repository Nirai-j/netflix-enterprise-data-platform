import pandas as pd

from simulator.validation.common import (
    check_duplicates,
    check_nulls,
    check_foreign_key
)


def run():

    accounts = pd.read_parquet(
        "simulator/output/account/accounts.parquet"
    )

    profiles = pd.read_parquet(
        "simulator/output/account/profiles.parquet"
    )

    check_duplicates(
        accounts,
        "account_id"
    )

    check_duplicates(
        profiles,
        "profile_id"
    )

    check_foreign_key(
        profiles,
        accounts,
        "account_id",
        "account_id"
    )

    check_nulls(accounts)
    check_nulls(profiles)

    print(
        "Account Validation Completed"
    )