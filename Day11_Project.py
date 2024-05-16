# Udemy 100 Projects in 100 days
# Day 11 Project
# BLACKJACK GAME
# Skills: Modules, Functions, Lists, While, For, Complex
# Notes: This was developed with no hints, approach is quite different to course final code. However my approach feels cleaner with less redundancy

import random
from os import system, name


def clear():
    """Used to clear screen.... believe no longer working as volume of python files have increased"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def add_card(player):
    """Appends the players card list with  a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player.append(random.choice(cards))


def get_scores(player):
    """Updates the score for the provided player"""
    # Note could just have used return sum(player), nothing else
    # Keeping this as an alternative for reference
    score = 0
    for card in player:
        score += card
    return score


def check_ace(player):
    """Checks if any card is an 11, then changes to a 1"""
    # Course approach was to .remove() and .append() This would change card order, mine is better
    for i in range(len(player)):
        if player[i] == 11:
            player[i] = 1


def print_final_hand(user, cpu):
    """Multiple common print lines called from multiple locations"""
    print(f"Your Final Hand:       {user}, final score: {get_scores(user)}")
    print(f"Computer's Final hand: {cpu}, final score: {get_scores(cpu)}")


def outcome(user_score, cpu_score):
    """Calculate winner, note accounted for BlackJack in main function"""
    if user_score > 21:
        return "You went over. You Lose"
    elif cpu_score > 21:
        return "Computer went over. You Win"
    elif user_score > cpu_score:
        return "You Win"
    elif user_score == cpu_score:
        return "Draw"
    else:
        return "You Lose"


def blackjack():
    """Main game code"""
    # declare empty lists for each player
    user = []
    cpu = []
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
        clear()
        # add 2 random cards for each player
        for x in range(2):
            add_card(user)
            add_card(cpu)
        # get total score for each player
        user_score = get_scores(user)
        cpu_score = get_scores(cpu)
        # check for blackjacks, if both, dealer wins
        if cpu_score == 21:
            print_final_hand(user, cpu)
            print("Dealer Wins: BlackJack")
        elif user_score == 21:
            print_final_hand(user, cpu)
            print("You Win: BlackJack")
        else:
            # if no blackjacks user can keep picking cards until they go bust
            should_continue = True
            while user_score < 21 and should_continue:
                print(f"Your cards: {user}, current score: {user_score}")
                print(f"Computer's first card: {cpu[0]}")
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    add_card(user)
                    user_score = get_scores(user)
                    if user_score > 21:
                        # if player score over 21 but they have an ace we change this to be 1 (instead of 11)
                        check_ace(user)
                        user_score = get_scores(user)
                else:
                    should_continue = False
            # once user has finished, if they are not bust, the dealer will draw cards unless score is at least 17
            if user_score <= 21:
                while cpu_score < 17:
                    add_card(cpu)
                    cpu_score = get_scores(cpu)
                    if cpu_score > 21:
                        check_ace(cpu)
                        cpu_score = get_scores(cpu)
            print_final_hand(user, cpu)
            print(outcome(user_score, cpu_score))
        blackjack()


blackjack()
