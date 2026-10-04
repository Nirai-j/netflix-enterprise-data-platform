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

    event_count = cfg["search_events"]

    profiles = pd.read_parquet(
        "simulator/output/account/profiles.parquet"
    )

    event_gen = IdGenerator("EVT")

    search_terms = [
        "stranger things",
        "dark",
        "money heist",
        "breaking bad",
        "narcos",
        "friends",
        "action movie",
        "comedy",
        "documentary"
    ]

    rows = []

    for _ in range(event_count):

        profile = profiles.sample(1).iloc[0]

        rows.append(
            {
                "event_id": event_gen.next_id(),
                "event_type": "SEARCH",
                "event_ts": fake.date_time_between(
                    start_date="-90d",
                    end_date="now"
                ),
                "schema_version": 1,

                "profile_id":
                    profile["profile_id"],

                "search_text":
                    random.choice(search_terms),

                "device_type":
                    random.choice(
                        [
                            "TV",
                            "MOBILE",
                            "TABLET",
                            "WEB"
                        ]
                    )
            }
        )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/playback/search_events.parquet"
    )

    return df


if __name__ == "__main__":
    generate()