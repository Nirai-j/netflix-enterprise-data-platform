from sqlalchemy import text

from source_systems.database.connection import get_engine


def generate():

    engine = get_engine()

    with engine.begin() as conn:

        conn.execute(
            text(
                """
                UPDATE payment.payment
                SET payment_status='REFUNDED',
                    updated_at=CURRENT_TIMESTAMP
                WHERE payment_id IN
                (
                    SELECT payment_id
                    FROM payment.payment
                    ORDER BY random()
                    LIMIT 10
                )
                """
            )
        )

    print("Payment updates generated.")