
from wordslist import words
import random

#Display the art
hangman_art = {0: ("  ",
                   "  ",
                   "  "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " ∣ ",
                   "   "),
               3: ("  o  ",
                   " /∣  ",
                   "     "),
               4: ("  o   ",
                   " /∣\\ ",
                   "      "),
               5: ("   o   ",
                   "  /|\\ ", 
                   "  /    "),
               6: ("   o   ",
                   "  /|\\ ",
                   "  / \\ ")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def play_again():
    while True:
        response = input('Do you want to continue? y/n ').lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print('Please enter y/n')
        

def main():
    while True:
        answer = random.choice(words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True

        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input")
                continue

            if guess in guessed_letters:
                print(f"{guess} is already guessed.")
                continue

            guessed_letters.add(guess)

            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        if i == 0:
                            hint[i] = guess.upper()
                        else:
                            hint[i] = guess
            else:
                wrong_guesses += 1

            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("YOU WIN!")
                is_running = False

            elif wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                display_answer(answer)
                print("YOU LOSE!")
                is_running = False
                
        if not play_again():
            print('Thanks for playing')
            break

if __name__ == "__main__":
    main()
