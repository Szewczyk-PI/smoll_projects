import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
    player_hand = random.choices(cards, k=2)
    dealer_hand = random.choices(cards, k=1)
    score = player_hand[0] + player_hand[1]
    print(f"Your cards: {player_hand}, current score: {score}")
    print(f"Dealer first card: {dealer_hand}")

    def draw(player_hand, dealer_hand, score):
        new_card = random.choice(cards)
        player_hand.append(new_card)
        score += new_card
        if score > 21:
            print(f"Your cards: {player_hand}, current score: {score}")
            print(f"Dealer first card: {dealer_hand}")
            print("You went over. You lose.")
            return False
        elif score <= 21:
            print(f"Your cards: {player_hand}, current score: {score}")
            print(f"Dealer first card: {dealer_hand}")
        return player_hand, dealer_hand, score

    while score <= 21:
        dec2 = input("Type 'y' to get another card, type 'n' to pass:\n ")
        if dec2 == "y":
            player_hand, dealer_hand, score = draw(player_hand, dealer_hand, score)
        elif dec2 == "n":
           break

    dealer_hand.extend(random.choices(cards, k=1))
    dealer_score = dealer_hand[0] + dealer_hand[1]
    print(f"Your cards: {player_hand}, current score: {score}")
    print(f"Dealer cards: {dealer_hand}, dealer score: {dealer_score}")
    if score > dealer_score:
        print("You win!")
    else:
        print("You lose!")


dec = input("Do you want to play Blackjack? (y/n): \n")

if dec == "y":
    game()
else:
    exit()
