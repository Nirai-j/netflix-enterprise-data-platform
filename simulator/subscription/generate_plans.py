import pandas as pd

from simulator.common.file_writer import FileWriter


def generate():

    plans = [
        {
            "plan_id": "PLAN_BASIC",
            "plan_name": "Basic",
            "monthly_price": 7.99,
            "currency": "USD",
            "max_screens": 1,
            "video_quality": "HD"
        },
        {
            "plan_id": "PLAN_STANDARD",
            "plan_name": "Standard",
            "monthly_price": 15.49,
            "currency": "USD",
            "max_screens": 2,
            "video_quality": "FULL_HD"
        },
        {
            "plan_id": "PLAN_PREMIUM",
            "plan_name": "Premium",
            "monthly_price": 22.99,
            "currency": "USD",
            "max_screens": 4,
            "video_quality": "UHD"
        }
    ]

    df = pd.DataFrame(plans)

    FileWriter.write_parquet(
        df,
        "simulator/output/subscription/plans.parquet"
    )

    return df


if __name__ == "__main__":
    generate()