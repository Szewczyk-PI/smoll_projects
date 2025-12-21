import random
words = ["aardvark", "baboon", "camel"]

word_pick = random.choice(words)
print(word_pick)

for word in word_pick:
    liczba = len(word_pick)
    print("_ " * liczba)
    guess = input("Podaj literę: ").lower()
    if (guess in word_pick):
        print("True")
    else:
        print("False")
