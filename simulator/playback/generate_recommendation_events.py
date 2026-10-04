import random
import pandas as pd

from faker import Faker

from simulator.common.id_generator import IdGenerator
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config

fake = Faker()


def generate():

    cfg = load_config(
        "simulator/config/volumes.yaml"
    )

    event_count = cfg[
        "recommendation_events"
    ]

    profiles = pd.read_parquet(
        "simulator/output/account/profiles.parquet"
    )

    titles = pd.read_parquet(
        "simulator/output/content/titles.parquet"
    )

    event_gen = IdGenerator("EVT")

    rows = []

    for _ in range(event_count):

        profile = profiles.sample(1).iloc[0]
        content = titles.sample(1).iloc[0]

        rows.append(
            {
                "event_id":
                    event_gen.next_id(),

                "event_type":
                    "RECOMMENDATION_SHOWN",

                "event_ts":
                    fake.date_time_between(
                        start_date="-90d",
                        end_date="now"
                    ),

                "schema_version": 1,

                "profile_id":
                    profile["profile_id"],

                "content_id":
                    content["content_id"],

                "rank":
                    random.randint(1, 20)
            }
        )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/playback/recommendation_events.parquet"
    )

    return df


if __name__ == "__main__":
    generate()