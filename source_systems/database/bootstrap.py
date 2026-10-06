from pathlib import Path

from source_systems.database.connection import get_engine


DDL_DIR = Path("source_systems/ddl")

DDL_FILES = [
    "account.sql",
    "subscription.sql",
    "payment.sql",
    "content.sql",
]


def bootstrap():
    engine = get_engine()

    raw_connection = engine.raw_connection()

    try:
        cursor = raw_connection.cursor()

        for ddl_file in DDL_FILES:

            path = DDL_DIR / ddl_file

            print(f"Applying {path}")

            sql = path.read_text(
                encoding="utf-8"
            )

            cursor.execute(sql)

        raw_connection.commit()

        print("Database bootstrap completed.")

    except Exception:
        raw_connection.rollback()
        raise

    finally:
        raw_connection.close()


if __name__ == "__main__":
    bootstrap()