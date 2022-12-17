import os
import art


def caesar(direction, text, shift):
    new_text = ""

    for char in text:
        if char not in alphabet:
            new_text += char
        else:
            index = alphabet.index(char)
            
            if direction == 'encode':
                new_index = (index + shift) % 26
            elif direction == 'decode':
                new_index = (index - shift) % 26
            
            new_text += alphabet[new_index]

    print(f"\nThe {direction}d message is:\n{new_text}\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = True


while restart == True:
    clear_screen()
    print(art.logo)
        
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    
    choice = (input("Would you like to run the Caesar Cipher again? (yes/no)\n")).lower()

    if choice == 'no':
        print("\nGoodbye!")
        restart = False
