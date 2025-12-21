import random
words = ["aardvark", "baboon", "camel"]

word_pick = random.choice(words)
print(word_pick)
liczba = len(word_pick)
placeholder = ""


for tak in range(liczba):
        placeholder += "- "
print(placeholder)

display = ""

for letter in word_pick:
    guess = input("Podaj literę: ").lower()
    if (letter == guess):
        display += guess
    else:
        display += "_ "
    print(display)