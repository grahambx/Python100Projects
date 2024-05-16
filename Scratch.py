
from random import randint
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add_card(player):
    """Returns a random card from deck"""
    player.append(cards[randint(0, 12)])


def update_scores(player):
    score = 0
    for card in player:
        score += card
    return score
    # could just have used return sum(player), nothing else


def check_ace(player):
    for i in range(len(player)):
        if player[i] == 11:
            player[i] = 1


def print_final_hand(user, cpu):
    print(f"Your Final Hand:       {user}, final score: {update_scores(user)}")
    print(f"Computer's Final hand: {cpu}, final score: {update_scores(cpu)}")


def outcome(user_score, cpu_score):
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
    user = []
    cpu = []
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
        clear()
        for x in range(2):
            add_card(user)
            add_card(cpu)
        user_score = update_scores(user)
        cpu_score = update_scores(cpu)
        if cpu_score == 21:
            print_final_hand(user, cpu)
            print("Dealer Wins: BlackJack")
        elif user_score == 21:
            print_final_hand(user, cpu)
            print("You Win: BlackJack")
        else:
            should_continue = True
            while user_score < 21 and should_continue:
                print(f"Your cards: {user}, current score: {user_score}")
                print(f"Computer's first card: {cpu[0]}")
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    add_card(user)
                    user_score = update_scores(user)
                    if user_score > 21:
                        check_ace(user)
                        user_score = update_scores(user)
                else:
                    should_continue = False
            if user_score <= 21:
                while cpu_score < 17:
                    add_card(cpu)
                    cpu_score = update_scores(cpu)
                    if cpu_score > 21:
                        check_ace(cpu)
                        cpu_score = update_scores(cpu)
            print_final_hand(user, cpu)
            print(outcome(user_score, cpu_score))
        blackjack()


blackjack()
