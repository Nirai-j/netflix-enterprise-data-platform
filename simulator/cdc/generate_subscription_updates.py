from sqlalchemy import text

from source_systems.database.connection import get_engine


def generate():

    engine = get_engine()

    with engine.begin() as conn:

        conn.execute(
            text(
                """
                UPDATE subscription.subscription
                SET status='CANCELLED',
                    updated_at=CURRENT_TIMESTAMP
                WHERE subscription_id IN
                (
                    SELECT subscription_id
                    FROM subscription.subscription
                    ORDER BY random()
                    LIMIT 25
                )
                """
            )
        )

    print("Subscription updates generated.")