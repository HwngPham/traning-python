from util import BirthdayUtility


class Game:
    SIMULATIONS_COUNT = 100_000

    def __init__(self, time_util):
        self.birthdays_count = 0
        self.birthdays = []
        self.simulation_count = 0
        self.simulation_results = []
        self.util = time_util

    def prompt_birthday_count(self):
        user_input = input('How many birthdays shall I generated? (Max 100)\n')
        is_valid_input = not user_input.isdecimal() or int(
            user_input) <= 0 or int(user_input) > 100
        if is_valid_input:
            print('Please enter a number from 0 to 100\n')
            return self.prompt_birthday_count()

        self.birthdays_count = int(user_input)
        self.execute()

    def execute(self):
        if self.birthdays_count == 0:
            return

        self.__generate_birthdays()
        if self.__check_occurence():
            for _ in range(Game.SIMULATIONS_COUNT):
                simulation_result = self.__run_simulation()
                self.simulation_results.append(simulation_result)
            self.__print_result()

    def __generate_birthdays(self):
        self.birthdays = [
            birthday.strftime('%b %d')
            for birthday in self.util.generate_birthdays(self.birthdays_count)
        ]

    def __run_simulation(self):
        if self.simulation_count == Game.SIMULATIONS_COUNT:
            print(f'{self.simulation_count} simulations run.')
            return -1

        if self.simulation_count % 10_000 == 0:
            print(f'{self.simulation_count} simulations run...')

        self.simulation_count += 1
        self.__generate_birthdays()
        for idx, birthday in enumerate(self.birthdays):
            temp_birthdays = [birthday for birthday in self.birthdays]
            temp_birthdays.pop(idx)
            if birthday in temp_birthdays:
                return idx

        return -1

    def __check_occurence(self):
        first_run_result = self.__run_simulation()
        if first_run_result == -1:
            print('Oops! There is no people have the same birthday')
            return False

        print(f'Here are {self.birthdays_count} birthdays:\n')
        print(", ".join(self.birthdays))
        print(
            f'\nIn this simulation, multiple people have a birthday on {self.birthdays[first_run_result]}')
        print(
            f'Generateing {self.birthdays_count} birthdays 100,000 times...')
        return True

    def __print_result(self):
        matching_counts = Game.SIMULATIONS_COUNT - \
            len([i for i in self.simulation_results if i == -1])

        print(
            f'Out of 100,000 simulations of {self.birthdays_count} people, there was a\n')
        print(
            f'matching birthday in that group {matching_counts} times. This means\n')
        print(
            f'that 23 people have a {matching_counts / Game.SIMULATIONS_COUNT * 100} % chance of\n')
        print('having a matching birthday in their group.\n')
        print('That\'s probably more than you would think!')


if __name__ == '__main__':
    time_util = BirthdayUtility()
    game = Game(time_util)
    game.prompt_birthday_count()
