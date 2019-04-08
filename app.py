"""Blackjack Game module has method to make it easier to code a blackjack game"""
from os import system, name
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.account import Account


def clear():
    """
     clear terminal
    :return:
    """
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('cls')


def play_blackjack(chips=Account('Chris', 500)):
    """
    Play BlackJack
    :param chips: object
    :return:
    """

    # request a name be entered if one isn't present
    while not len(chips.name):
        try:
            named = input('What\'s your name? ')

            if named.isalpha():
                chips.name = named
                break
            else:
                print(f"{named} is not a valid name, please enter a valid name")
                continue

        except:
            print('Sorry something went wrong, please try and input your name again')
            continue

    # Add fund to account if none is present
    if not chips.has_funds():
        chips.add_funds()
    # Add bet if none has been placed
    while not chips.has_bet():
        chips.make_bet()

    # Build deck and shuffle
    deck = Deck()
    deck.shuffle()

    deal_count = 1
    player = Hand()
    dealer = Hand()
    player.cards = []
    dealer.cards = []
    # Start first phase of the dealing
    while deal_count <= 4:
        deal_count += 1
        if deal_count % 2 == 0:
            if deal_count == 4:
                the_fourth_card = deck.deal()
                the_fourth_card.hide_card()
                dealer.add_card(the_fourth_card)
            else:
                dealer.add_card(deck.deal())

        else:
            player.add_card(deck.deal())

    # Second phase of the dealing
    while True:
        # display cards
        clear()
        print(chips.name + ': ')
        print(player)
        print('Dealers: ')
        print(dealer)

        if player.bust():
            break
        if player.next_move():
            player.add_card(deck.deal())
            continue
        else:
            break

    # change view permissions
    for card in dealer.cards:
        card.show_card()

    # Once player finishes turn continue to deal dealers hand
    while True:
        # display cards
        clear()
        print(chips.name + ': ')
        print(player)
        print('Dealers: ')
        print(dealer)

        if dealer.bust():
            break
        if player.bust():
            break
        if dealer.total() > player.total():
            break
        else:
            dealer.add_card(deck.deal())
            continue

    # display results and finalise transaction
    if player.bust():
        clear()
        chips.subtract()
        print(
            f"{chips.name} you lost this one\n\nYour new Balance {chips.balance()}\n"
            f"{chips.name}: {player}"
            f"Dealers: {dealer}"
            f"\nYour Score {player.total()}\nDealers Score {dealer.total()}"
        )

    elif player.total() < dealer.total() and not dealer.bust():
        clear()
        chips.subtract()
        print(
            f"{chips.name} the dealer beat your score\n\nYour new Balance {chips.balance()}\n"
            f"{chips.name}: {player}"
            f"Dealers: {dealer}"
            f"\nYour Score {player.total()}\nDealers Score {dealer.total()}"
        )

    else:
        clear()
        chips.add()
        print(
            f"{chips.name} you won!\n\nYour new Balance {chips.balance()}\n"
            f"{chips.name}: {player}"
            f"Dealers: {dealer}"
            f"\nYour Score {player.total()}\nDealers Score {dealer.total()}"
        )

    # Do they want to replay
    while True:
        try:
            replay = input('Do you want to play again? ').upper()

            if replay == 'YES':
                play_blackjack()
                break
            elif replay == 'NO':
                print(f'{chips.name} thank you for playing and we look forward to seeing you again')
                break
            else:
                print('We didn\'t understand your request, a YES or NO is desired')
                continue
        except ValueError:
            print('Invalid Input: We didn\'t recognise your request please try again YES or No')
            continue


play_blackjack()
