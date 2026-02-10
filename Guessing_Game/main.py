import random
from art import logo
print(logo)
print("Welcome to Gussing Game!")
number = random.randrange(1, 101)
print("I'm thinking of a number beetwen 1 and 100")
difficulty = input("Chose difficulty, type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

is_game = True

print(f"You have {attempts} attempts remaining to guess the number.")

def check_ans(guess , number):
    if(guess < number):
        print("Too low.")
    elif(guess > number):
        print("Too high.")

while is_game:
    guess = int(input("Make a guess: "))
    check_ans(guess, number)
    attempts = attempts - 1
    if (attempts == 0):
        print("You've run out of guesses")
        is_game = False
    elif(guess == number):
        print(f"You got it! The answer was {number}")
        is_game = False