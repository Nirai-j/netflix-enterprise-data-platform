import pandas as pd

from simulator.validation.common import (
    check_duplicates,
    check_foreign_key
)


def run():

    titles = pd.read_parquet(
        "simulator/output/content/titles.parquet"
    )

    seasons = pd.read_parquet(
        "simulator/output/content/seasons.parquet"
    )

    episodes = pd.read_parquet(
        "simulator/output/content/episodes.parquet"
    )

    check_duplicates(
        titles,
        "content_id"
    )

    check_duplicates(
        seasons,
        "season_id"
    )

    check_duplicates(
        episodes,
        "episode_id"
    )

    check_foreign_key(
        seasons,
        titles,
        "content_id",
        "content_id"
    )

    check_foreign_key(
        episodes,
        seasons,
        "season_id",
        "season_id"
    )

    print(
        "Content Validation Completed"
    )