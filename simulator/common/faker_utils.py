from faker import Faker

fake = Faker()


def country():
    return fake.country_code()


def language():
    return fake.language_code()


def acquisition_channel():
    return fake.random_element(
        [
            "WEB",
            "MOBILE",
            "TV_APP",
            "PARTNER"
        ]
    )