import random
import pandas as pd

from simulator.common.id_generator import IdGenerator
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config


def generate():

    cfg = load_config(
        "simulator/config/volumes.yaml"
    )

    titles = pd.read_parquet(
        "simulator/output/content/titles.parquet"
    )

    season_gen = IdGenerator("SEA")

    rows = []

    min_seasons = cfg["seasons_per_series"]["min"]
    max_seasons = cfg["seasons_per_series"]["max"]

    series_df = titles[
        titles["content_type"] == "SERIES"
    ]

    for _, title in series_df.iterrows():

        season_count = random.randint(
            min_seasons,
            max_seasons
        )

        for season_num in range(
            1,
            season_count + 1
        ):

            rows.append(
                {
                    "season_id": season_gen.next_id(),
                    "content_id":
                        title["content_id"],
                    "season_number":
                        season_num
                }
            )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/content/seasons.parquet"
    )

    return df


if __name__ == "__main__":
    generate()