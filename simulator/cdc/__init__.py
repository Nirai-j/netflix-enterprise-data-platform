import json
import math
import random
from datetime import datetime, timezone
from uuid import uuid4

import pandas as pd

from simulator.common.file_writer import FileWriter


EVENT_COLUMNS = [
    "event_id",
    "entity",
    "operation",
    "record_key",
    "event_timestamp",
    "before",
    "after",
]


def create_update_events(
    records,
    entity,
    key_column,
    update_record,
    fraction=0.05,
    seed=42,
):
    if not 0 <= fraction <= 1:
        raise ValueError("fraction must be between 0 and 1")
    if key_column not in records.columns:
        raise ValueError(f"Missing key column: {key_column}")

    count = min(len(records), math.ceil(len(records) * fraction))
    selected = random.Random(seed).sample(range(len(records)), count)
    events = []

    for position in selected:
        before = records.iloc[position].to_dict()
        after = update_record(before.copy())
        events.append(
            {
                "event_id": str(uuid4()),
                "entity": entity,
                "operation": "UPDATE",
                "record_key": str(before[key_column]),
                "event_timestamp": datetime.now(timezone.utc).isoformat(),
                "before": json.dumps(before, default=str),
                "after": json.dumps(after, default=str),
            }
        )

    return pd.DataFrame(events, columns=EVENT_COLUMNS)


def write_update_events(events, output_path):
    FileWriter.write_parquet(events, output_path)
    return events