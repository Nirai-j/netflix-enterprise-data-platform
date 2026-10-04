from faker import Faker

fake = Faker()


def random_date():
    return fake.date_between(
        start_date="-3y",
        end_date="today"
    )