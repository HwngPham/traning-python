from random import randint


intro_text = """I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
Pico        One digit is correct but in the wrong position.
Fermi       One digit is correct and in the right position.
Bagels      No digit is correct.
I have thought up a number.
You have 10 guesses to get it."""


class Game:
    DIGIT_CORRECT = 'Fermi'
    DIGIT_CORRECT_BUT_WRONG_POSITION = 'Pico'
    DIGIT_INCORRECT = 'Bagels'
    MAX_GUESS_COUNT = 10
    GAME_OVER_SIGNAL = -1

    def __init__(self):
        self.guess_count = 0
        self.target_num = str(randint(100, 999))
        print(intro_text)
        print(f'Cheat: {self.target_num}')

    def execute(self):
        if self.guess_count == Game.MAX_GUESS_COUNT:
            print('Game over!')
            return Game.GAME_OVER_SIGNAL

        guess = input(f'Guess #{self.guess_count}:\n')
        is_valid_guess = self.__validate_input(guess)

        if is_valid_guess:
            result = self.__check_guess(guess)
            if len(result) == len(Game.DIGIT_CORRECT) * 3 + 2:
                print(f'Congratulation! It\'s {self.target_num}')
                return Game.GAME_OVER_SIGNAL
            else:
                print(result)

        return self.execute()

    def __check_guess(self, num):
        digits_check_result = []
        for idx, digit in enumerate(num):
            if digit in self.target_num:
                digits_check_result.append(
                    Game.DIGIT_CORRECT if digit == self.target_num[idx]
                    else Game.DIGIT_CORRECT_BUT_WRONG_POSITION
                )

        self.guess_count += 1
        return Game.DIGIT_INCORRECT if len(digits_check_result) == 0 \
            else " ".join(digits_check_result)

    def __validate_input(self, num):
        try:
            guess = int(num)
        except:
            print('Please enter a valid number!')
            return False

        if guess < 100 or guess > 999:
            print('Please enter a 3-digits number!')
            return False

        return True


if __name__ == '__main__':
    while True:
        game = Game()
        if game.execute() == Game.GAME_OVER_SIGNAL:
            play_again_prompt = input(
                'Do you want to play again? (yes or no) ')
            while play_again_prompt not in ['yes', 'no']:
                play_again_prompt = input('Please answer [yes] or [no]: ')
            if play_again_prompt == 'yes':
                continue
            else:
                break
