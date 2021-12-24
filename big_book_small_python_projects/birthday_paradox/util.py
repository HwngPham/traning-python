from random import randint
from datetime import date, timedelta


class BirthdayUtility:
    def __init__(self):
        self.base_date = self.get_random_date()

    def get_random_date(self):
        return date(
            year=2000,  # Year does not matter
            month=randint(1, 12),
            day=randint(1, 28),  # Ensure it is not 30th on January
        )

    def get_random_date_range(self):
        # Range duration does not matter, as long ranges are vary
        return timedelta(randint(1, 10e3))

    def generate_birthdays(self, amount):
        return [self.base_date + self.get_random_date_range() for _ in range(amount)]
