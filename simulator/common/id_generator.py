from itertools import count


class IdGenerator:

    def __init__(self, prefix: str):
        self.prefix = prefix
        self.counter = count(1)

    def next_id(self):
        return f"{self.prefix}{next(self.counter):06d}"