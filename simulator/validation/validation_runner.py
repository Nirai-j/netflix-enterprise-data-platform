from simulator.validation.validate_accounts import run as validate_accounts

from simulator.validation.validate_content import run as validate_content

from simulator.validation.validate_revenue import run as validate_revenue

from simulator.validation.validate_playback import run as validate_playback


def run():

    print("\nAccounts Validation")
    validate_accounts()

    print("\nContent Validation")
    validate_content()

    print("\nRevenue Validation")
    validate_revenue()

    print("\nPlayback Validation")
    validate_playback()

    print("\nAll Validations Passed")


if __name__ == "__main__":
    run()