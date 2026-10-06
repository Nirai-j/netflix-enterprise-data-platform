from .ddl import create_schema

from .load_accounts import load as load_accounts
from .load_content import load as load_content
from .load_subscription import load as load_subscription
from .load_payment import load as load_payment


def bootstrap():

    create_schema()

    load_accounts()
    load_content()
    load_subscription()
    load_payment()

    print("Aurora Bootstrap Completed")


if __name__ == "__main__":
    bootstrap()