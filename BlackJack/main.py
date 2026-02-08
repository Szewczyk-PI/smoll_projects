import random
from art import logo

def deal_card():
    """ Deal a card randomly """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """ Calculate the score of a card """
    if sum(cards) == 2 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compere(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent have a BlackJack"
    elif u_score == 0:
        return "Win, BlackJack!"
    elif u_score > 21:
        return "Lose, went over"
    elif c_score > 21:
        return "Win, Opponent went over"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards {user_cards}, Your score is {user_score}")
        print(f"Computer First Card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card , type 'n' to pass ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your hands: {user_cards}, final score: {user_score}")
    print(f"Computer hands: {computer_cards}, final score: {computer_score}")
    print(compere(user_score, computer_score))

while input("Do You want to play BlackJack? Type 'y' or 'n' ") == "y":
    print(logo)
    play_game()