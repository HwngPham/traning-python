class Card:
    HEART_SYMBOL = chr(9829)
    DIAMON_SYMBOL = chr(9830)
    SPADE_SYMBOL = chr(9824)
    CLUB_SYMBOL = chr(9827)
    BLANK_SYMBOL = '#'

    ACE_VALUE = 1
    JACK_VALUE = 11
    QUEEN_VALUE = 12
    KING_VALUE = 13

    def __init__(self, type, value):
        self.type = type
        self.value = str(value)
        self.front_presentation = self.__gen_front_presentation()
        self.back_presentation = self.__gen_back_presentation()
        self.current_presentation = self.front_presentation

    def __gen_front_presentation(self):
        display_value = self.value
        display_type = self.type
        # TODO: change card presentation to list for merging ability with another card row-by-row
        return '____\n' \
            + f'|{display_value.ljust(3)}|\n' \
            + f'| {display_type} |\n' \
            + f'|{display_value.rjust(3, "_")}|'

    def __gen_back_presentation(self):
        return '____\n' \
            + f'|{Card.BLANK_SYMBOL*2} |\n' \
            + f'| {Card.BLANK_SYMBOL} |\n' \
            + f'|_{Card.BLANK_SYMBOL*2}|'

    def flip(self):
        self.current_presentation = self.back_presentation \
            if self.current_presentation == self.front_presentation \
            else self.front_presentation

    def __str__(self):
        return self.current_presentation
