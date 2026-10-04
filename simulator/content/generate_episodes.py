import random
import pandas as pd

from simulator.common.id_generator import IdGenerator
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config


def generate():

    cfg = load_config(
        "simulator/config/volumes.yaml"
    )

    seasons = pd.read_parquet(
        "simulator/output/content/seasons.parquet"
    )

    episode_gen = IdGenerator("EPI")

    rows = []

    min_ep = cfg["episodes_per_season"]["min"]
    max_ep = cfg["episodes_per_season"]["max"]

    for _, season in seasons.iterrows():

        episode_count = random.randint(
            min_ep,
            max_ep
        )

        for ep_num in range(
            1,
            episode_count + 1
        ):

            rows.append(
                {
                    "episode_id":
                        episode_gen.next_id(),
                    "season_id":
                        season["season_id"],
                    "episode_number":
                        ep_num,
                    "duration_minutes":
                        random.randint(
                            20,
                            60
                        )
                }
            )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/content/episodes.parquet"
    )

    return df


if __name__ == "__main__":
    generate()