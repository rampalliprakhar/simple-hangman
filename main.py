import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)

correct_guess = []
incorrect_guesses = []

def game_over_message(is_win, chosen_word):
    if is_win:
        print("****************************YOU WIN****************************")
    else:
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

while lives > 0:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    while len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid letter (one letter only).")
        guess = input("Guess a letter: ").lower()

    if guess in correct_guess or guess in incorrect_guesses:
        print(f"You have already guessed {guess}")
        continue

    if guess in chosen_word:
        correct_guess.append(guess)
    else:
        incorrect_guesses.append(guess)
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    display = "".join([letter if letter in correct_guess else "_" for letter in chosen_word])
    print("Word to guess: " + display)

    if "_" not in display:
        game_over_message(True, chosen_word)
        break

    print(stages[lives])

if lives == 0:
    game_over_message(False, chosen_word)