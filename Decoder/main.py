alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cesar(direction, text, shift):
    if direction == 'encode':
        cipher_text = ""
        for letter in text:
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")
    elif direction == 'decode':
        text1 = ""
        for letter in text:
            shifted_position = alphabet.index(letter) - shift
            shifted_position %= len(alphabet)
            text1 += alphabet[shifted_position]
        print(f"Here is the decoded result: {text}")
    else:
        print("Wrong Input")

cesar(direction, text, shift)