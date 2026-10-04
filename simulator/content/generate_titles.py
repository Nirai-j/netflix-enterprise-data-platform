import random
import pandas as pd

from faker import Faker

from simulator.common.id_generator import IdGenerator
from simulator.common.file_writer import FileWriter
from simulator.common.config_loader import load_config

fake = Faker()


def generate():

    cfg = load_config("simulator/config/volumes.yaml")

    title_count = cfg["titles"]

    title_gen = IdGenerator("TTL")

    genres = [
        "ACTION",
        "COMEDY",
        "DRAMA",
        "THRILLER",
        "SCI_FI",
        "ROMANCE",
        "DOCUMENTARY"
    ]

    rows = []

    for _ in range(title_count):

        content_type = random.choice(
            ["MOVIE", "SERIES"]
        )

        rows.append(
            {
                "content_id": title_gen.next_id(),
                "title_name": fake.sentence(
                    nb_words=3
                ).replace(".", ""),
                "content_type": content_type,
                "genre": random.choice(genres),
                "release_year": random.randint(
                    1990,
                    2025
                ),
                "rating": random.choice(
                    [
                        "G",
                        "PG",
                        "PG13",
                        "R"
                    ]
                ),
                "duration_minutes": random.randint(
                    60,
                    180
                ) if content_type == "MOVIE" else None
            }
        )

    df = pd.DataFrame(rows)

    FileWriter.write_parquet(
        df,
        "simulator/output/content/titles.parquet"
    )

    return df


if __name__ == "__main__":
    generate()