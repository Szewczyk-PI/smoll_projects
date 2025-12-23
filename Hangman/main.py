import random
words = ["aardvark", "baboon", "camel"]

word_pick = random.choice(words)

stages = [
    # Etap 0 - pełny wisielec (przegrana)
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     / \
       -
    """,
    # Etap 1 - jedna noga
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     /
       -
    """,
    # Etap 2 - tułów i ręce
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |
       -
    """,
    # Etap 3 - tułów i jedna ręka
    r"""
       --------
       |      |
       |      O
       |     \|
       |
       |
       -
    """,
    # Etap 4 - tułów
    r"""
       --------
       |      |
       |      O
       |      |
       |
       |
       -
    """,
    # Etap 5 - głowa
    r"""
       --------
       |      |
       |      O
       |
       |
       |
       -
    """,
    # Etap 6 - początek (pusta szubienica)
    r"""
       --------
       |      |
       |
       |
       |
       |
       -
    """
]

correct = []
lives = 6
game_over = False

# Pokaż początkowy stan gry
placeholder = "_" * len(word_pick)
print(stages[lives])

while not game_over:
    guess = input("\n Chose letter: ").lower()

    # Sprawdź czy litera jest w słowie
    if guess in word_pick:
        correct.append(guess)
    else:
        lives -= 1

    # Zbuduj wyświetlane słowo
    display = ""
    for letter in word_pick:
        if letter in correct:
            display += letter
        else:
            display += "_"

    print(f"\n{display}")
    print(stages[lives])

    # Sprawdź warunki końca gry
    if "_" not in display:
        game_over = True
        print("\n You Win!")
        print(f"Word: {word_pick}")

    if lives == 0:
        game_over = True
        print("\n You lose!")
        print(f"Word: {word_pick}")