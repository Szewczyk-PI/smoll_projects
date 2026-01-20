import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    game = input("Do you want to play blackjack? (y/n): ")
    if game != "y":
        break

    card = 0
    player_cards = random.choices(cards, k=2)
    card =+ 2
    dealer_cards = [random.choice(cards)]
    score_player = player_cards[0] + player_cards[1]
    score_dealer = dealer_cards[0]


    def add_one(score_player, player_cards, card):
        if score_player < 21:
            new_card = random.choice(cards)
            player_cards.append(new_card)
            score_player += new_card
            card += 1
            print(f"Your cards: {player_cards}, current score: {score_player} \n Computer cards: {dealer_cards}")
        return score_player, player_cards, card

    print(f"Your cards: {player_cards}, current score: {score_player} \n Computer cards: {dealer_cards}")
    while True:
        draw = input("Do you want to draw? (y/n): ")
        if draw == "y":
            score_player, player_cards, card = add_one(score_player, player_cards, card)
            if score_player > 21:
                print("Bust! You lose!")
                break
            elif card == 4:
                break
        else:
            break

    if score_player < 21:
        dealer_cards.append(random.choice(cards))
        dealer_score = dealer_cards[0] + dealer_cards[1]
        print(f"Your cards: {player_cards}, current score: {score_player}")
        print(f"Dealer cards: {dealer_cards}, dealer score: {dealer_score}")
        if score_player > dealer_score:
            print("You Win!")
        elif score_player < dealer_score:
            print("You Lose!")
        elif score_player == dealer_score:
            print("Draw!")

    print()


