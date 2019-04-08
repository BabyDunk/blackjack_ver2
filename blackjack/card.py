class Card:
    """
    Card object with variety of methods
    """

    def __init__(self, card):
        self.card = card

    def __str__(self):
        """
        Prints card if object is true
        :return: str
        """
        if self.is_show():
            show_cards = self.card_rank() + " of " + self.card_suit()
        else:
            show_cards = 'Card Face Down'
        return show_cards

    def card(self):
        """
        Returns card
        :return: list
        """
        return self.card

    def card_suit(self):
        """
        Returns card suit
        :return: str
        """
        return self.card[0]

    def card_rank(self):
        """
        Returns card rank
        :return: str
        """
        return self.card[1]

    def card_val(self):
        """
        Return card value
        :return: int
        """
        return self.card[2]

    def is_show(self):
        """
        Check if card should be visible
        :return: boolean
        """
        return self.card[3]

    def show_card(self):
        """
        Set card to be visible
        :return: none
        """
        self.card[3] = True

    def hide_card(self):
        """
        Set card to not be visible
        :return: none
        """
        self.card[3] = False
