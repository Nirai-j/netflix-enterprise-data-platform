from simulator.cdc.generate_account_updates import generate as account_updates
from simulator.cdc.generate_subscription_updates import generate as subscription_updates
from simulator.cdc.generate_payment_updates import generate as payment_updates


def run():

    account_updates()

    subscription_updates()

    payment_updates()

    print("CDC changes completed.")


if __name__ == "__main__":
    run()