from random import shuffle, randint
from card import Card


class Deck:
    CARD_TYPES = [
        Card.HEART_SYMBOL,
        Card.DIAMON_SYMBOL,
        Card.SPADE_SYMBOL,
        Card.CLUB_SYMBOL]
    CARD_VALUES = [n for n in range(1, 14)]

    def __init__(self):
        self.cards = self.__gen_cards()

    def __gen_cards(self):
        cards = []
        for card_type in Deck.CARD_TYPES:
            for card_value in Deck.CARD_VALUES:
                card = Card(card_type, card_value)
                cards.append(card)
        return cards

    def suffle(self):
        shuffle(self.cards)

    def take_one_card_out(self):
        chosen_card_idx = randint(1, len(self.cards))
        chosen_card = self.cards[chosen_card_idx]
        self.cards = self.cards[:chosen_card_idx] + \
            self.cards[chosen_card_idx+1:]
        return chosen_card
