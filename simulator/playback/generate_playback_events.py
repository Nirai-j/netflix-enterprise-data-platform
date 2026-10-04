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

    event_count = cfg["playback_events"]

    profiles = pd.read_parquet(
        "simulator/output/account/profiles.parquet"
    )

    titles = pd.read_parquet(
        "simulator/output/content/titles.parquet"
    )

    event_gen = IdGenerator("EVT")
    session_gen = IdGenerator("SES")

    device_types = [
        "TV",
        "MOBILE",
        "TABLET",
        "WEB"
    ]

    qualities = [
        "SD",
        "HD",
        "FULL_HD",
        "UHD"
    ]

    event_types = [
        "PLAY",
        "PAUSE",
        "RESUME",
        "STOP",
        "COMPLETE"
    ]

    rows = []

    for _ in range(event_count):

        profile = profiles.sample(1).iloc[0]
        content = titles.sample(1).iloc[0]

        rows.append(
            {
                "event_id": event_gen.next_id(),
                "event_type": random.choice(event_types),
                "event_ts": fake.date_time_between(
                    start_date="-90d",
                    end_date="now"
                ),
                "schema_version": 1,

                "session_id": session_gen.next_id(),
                "profile_id": profile["profile_id"],
                "content_id": content["content_id"],

                "device_type":
                    random.choice(device_types),

                "quality":
                    random.choice(qualities),

                "position_seconds":
                    random.randint(0, 7200)
            }
        )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/playback/playback_events.parquet"
    )

    return df


if __name__ == "__main__":
    generate()