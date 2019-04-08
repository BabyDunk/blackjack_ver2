class Account:
    """
    Account object with variety of methods
    """

    def __init__(self, name='', bank=0):
        self.name = name
        self.bank = bank
        self.bet = 0

    def __str__(self):
        """
        When printed will return account balance
        :return: str
        """
        return f"Account Balance: {self.bank}"

    def bet(self, bet):
        """
        Set bet
        :param bet: number
        :return: none
        """
        self.bet = bet

    def has_bet(self):
        """
        Checks if bet has been set
        :return: boolean
        """
        return self.bet > 0

    def add(self):
        """
        Add bet value to balance
        :return: number
        """
        self.bank += self.bet
        self.bet = 0
        return self.bank

    def subtract(self):
        """
        Subtracts bet value from balance
        :return: number
        """
        self.bank -= self.bet
        self.bet = 0
        return self.bank

    def balance(self):
        """
        Return balance
        :return: number
        """
        return self.bank

    def has_funds(self):
        """
        Check if balances has value
        :return: boolean
        """
        return self.bank > 0

    def make_bet(self):
        """
        Checks if bet has been set or if bet has not been set it will request a bet value be entered
        :return: none
        """
        while True:
            try:
                betting = int(input('How much do you want to bet? '))

                if betting > 0:
                    if betting > self.bank:
                        print(f"{betting} has exceed the your balance of {self.bank}, please select a lower bet value")
                        continue
                    else:
                        self.bet = betting
                        break
                else:
                    print('You need to add a positive number if you want to bet')
                    continue
            except ValueError:
                print("Invalid Input: please be sure to enter a number value.")
                continue

    def add_funds(self):
        """
        Checks if there are funds. if not then request funds be added
        :return: none
        """
        while True:
            try:
                funding = int(input('How much would you like to add to your account? '))

                if funding > 0:
                    self.bank = funding
                    break
                else:
                    print('You need to add a positive number if you want to add funds to your balance')
                    continue
            except ValueError:
                print("Invalid Input: please be sure to enter a number value.")
                continue
