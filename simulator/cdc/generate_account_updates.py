import random
from sqlalchemy import text

from source_systems.database.connection import get_engine


def generate():

    engine = get_engine()

    countries = [
        "US",
        "UK",
        "IN",
        "CA",
        "AU"
    ]

    with engine.begin() as conn:

        conn.execute(
            text(
                """
                UPDATE account.account
                SET country = :country,
                    updated_at = CURRENT_TIMESTAMP
                WHERE account_id IN (
                    SELECT account_id
                    FROM account.account
                    ORDER BY random()
                    LIMIT 50
                )
                """
            ),
            {
                "country": random.choice(countries)
            }
        )

    print("Account updates generated.")