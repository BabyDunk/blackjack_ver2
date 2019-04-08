class Hand:
    """
    Hand object with variety of methods
    """
    initial_deal = True
    card_count = 0

    def __init__(self):
        self.cards = []

    def __str__(self):
        """
        Prints cards in hand
        :return: str
        """
        hand_print = ""
        for card in self.cards:
            hand_print += "\t" + card.__str__() + '\n'

        return "Cards in hand:\n" + hand_print + '\n'

    def add_card(self, card):
        """
        Add a card to the hand
        :param card: object
        :return: none
        """
        self.cards.append(card)

    def total(self):
        """
        Calculate the value of hand
        :return: number
        """
        total = 0
        aces = 0
        for val in self.cards:
            if val.card_val() == 11:
                aces += 1

            total += val.card_val()

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def bust(self):
        """
        Check if hand if bust
        :return: boolean
        """
        return self.total() > 21

    @staticmethod
    def next_move():
        """
        Check to see what the next move is HIT or STICK
        :return: boolean
        """
        while True:
            move = input('Do you want to HIT or STICK? ').upper()

            if move == 'HIT':
                return True
            elif move == 'STICK':
                return False
            else:
                print('Sorry i didn\'t recognise that, please tell me again')
                continue
