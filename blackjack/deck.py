from random import shuffle
from blackjack.card import Card


class Deck:
    """
    Deck object with variety of methods
    """

    def __init__(self):
        self.deck = []
        self.build_deck()

    def __str__(self):
        """
        Prints deck
        :return: str
        """
        deck_print = ''
        for card in self.deck:
            deck_print += f'\n' + card.__str__()

        return "The deck has:\n\n" + deck_print

    def build_deck(self):
        """
        Builds deck
        :return: list
        """
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

        for suit in suits:
            for i, val in enumerate(('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
                                     'Queen', 'King', 'Ace')):

                if val in ['Jack', 'Queen', 'King']:
                    self.deck.append(Card([suit, val, 10, True]))
                elif val in ['Ace ']:
                    self.deck.append(Card([suit, val, 11, True]))
                else:
                    self.deck.append(Card([suit, val, (i + 2), True]))

        return self.deck

    def shuffle(self):
        """
        Shuffles deck
        :return: list
        """
        shuffle(self.deck)

    def deal(self):
        """
        Pops a single card from the deck
        :return: object
        """
        return self.deck.pop(0)
