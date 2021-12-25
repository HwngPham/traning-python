from deck import Deck


class Action:
    TAKE_ANOTHER_CARD = 'h'
    STOP_TAKING_CARD = 's'
    DOUBLE_DOWN_BET = 'd'


class Game:
    INITIAL_MONEY = 5000
    MAX_POINT = 21
    RULE = """
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.
    """

    def __init__(self, deck):
        self.total_money = Game.INITIAL_MONEY
        self.deck = deck
        self.player_cards = []
        self.dealer_cards = []
        # player get an additional card
        # dealer reveals current card without draw anymore
        self.doubled_down = False
        self.current_bet_amount = 0

    def show_rules(self):
        print(Game.RULE)

    def show_result(self):
        print('Game over!\n')
        print(f'Total money: {self.total_money}\n')
        if self.total_money > Game.INITIAL_MONEY:
            print('CONGRATULATION!')
        else:
            print('Good luck next time!')

    def execute(self):
        self.show_rules()
        while True:
            print(f'Money: {self.total_money}')
            user_input = input('How much do you bet? (1-5000, or QUIT)\n')
            is_valid_bet_amount = user_input.isdecimal() \
                and int(user_input) > 0 \
                and int(user_input) < self.total_money \
                and int(user_input) < Game.INITIAL_MONEY

            if user_input.upper() == 'QUIT':
                self.show_result()
                break

            if not is_valid_bet_amount:
                print('PLEASE ENTER A VALID AMOUNT!\n')
                continue

            print(f'You bet: {user_input}')
            self.current_bet_amount = int(user_input)
            self.__start_1st_round()
            self.__start_2nd_round()
            self.__clean_hands()

    def __clean_hands(self):
        self.player_cards = []
        self.dealer_cards = []
        self.doubled_down = False

    def __show_player_hand(self):
        player_point = sum([int(card.value)
                           for card in self.player_cards]) % Game.MAX_POINT
        print(f'Player: {player_point}\n')
        for card in self.player_cards:
            print(card)

    def __show_dealer_hand(self, hidden=True):
        dealer_point = '???' if hidden else \
            sum([int(card.value)
                for card in self.dealer_cards]) % Game.MAX_POINT
        print(f'DEALER: {dealer_point}\n')
        for card in self.dealer_cards:
            print(card)

    def __start_1st_round(self):
        print('====================== INITIAL DEAL ======================')
        self.deck.suffle()
        for _ in range(0, 2):
            self.player_cards.append(
                self.deck.take_one_card_out()
            )
            self.dealer_cards.append(
                self.deck.take_one_card_out()
            )
        self.dealer_cards[0].flip()

        self.__show_dealer_hand()
        self.__show_player_hand()

    def __start_2nd_round(self):
        print('====================== PLAYER ACTION =====================')
        user_input = input('(H)it, (S)tand, (D)ouble down\n')
        if user_input not in ['h', 's', 'd', 'H', 'S', 'D']:
            return self.__start_2nd_round()

        if user_input in ['d', 'D']:
            self.doubled_down = True
            self.current_bet_amount *= 2
            self.player_cards.append(
                self.deck.take_one_card_out()
            )
            print(f'You raised your bet to {self.current_bet_amount}\n')
            return self.__start_3rd_round()

        if user_input in ['s', 'S']:
            return self.__start_3rd_round()

        if user_input in ['h', 'H']:
            self.player_cards.append(
                self.deck.take_one_card_out()
            )

        self.__start_3rd_round()

    def __start_3rd_round(self):
        print('====================== BET SETTLED =====================')
        if not self.doubled_down:
            self.dealer_cards.append(
                self.deck.take_one_card_out()
            )

        self.dealer_cards[0].flip()
        self.__show_dealer_hand(hidden=False)
        self.__show_player_hand()

        player_point = sum([int(card.value)
                           for card in self.player_cards]) % Game.MAX_POINT
        dealer_point = sum([int(card.value)
                           for card in self.dealer_cards]) % Game.MAX_POINT
        if player_point > dealer_point or player_point == 0:
            self.total_money += self.current_bet_amount
            print(f'Win! You\'ve gained {self.current_bet_amount}\n')
        else:
            self.total_money -= self.current_bet_amount
            print(f'Oops! You\'ve lost {self.current_bet_amount}\n')


if __name__ == '__main__':
    deck = Deck()
    game = Game(deck)
    game.execute()
