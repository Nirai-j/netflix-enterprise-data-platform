import pandas as pd


def check_duplicates(df, column_name):

    duplicate_count = df.duplicated(
        subset=[column_name]
    ).sum()

    print(
        f"[DUPLICATES] {column_name}: {duplicate_count}"
    )

    return duplicate_count == 0


def check_nulls(df):

    null_count = df.isnull().sum().sum()

    print(
        f"[NULLS] Total: {null_count}"
    )

    return null_count == 0


def check_foreign_key(
    child_df,
    parent_df,
    child_key,
    parent_key
):

    invalid_count = (
        ~child_df[child_key].isin(
            parent_df[parent_key]
        )
    ).sum()

    print(
        f"[FK] {child_key}->{parent_key}: {invalid_count}"
    )

    return invalid_count == 0