# Simple Hangman

## Overview

- The **Simple Hangman** project is a Python-based implementation of the classic hangman game. 
- The user guesses a word one letter at a time, with a limited number of incorrect guesses allowed. 
- If the player guesses all the letters correctly before running out of lives, they win. 
- If they run out of lives, they lose.

## Features

- Randomly selects a word from a predefined list
- Displays a hanging man as the player loses lives
- Tracks correct and incorrect guesses
- Provides feedback after each guess

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/rampalliprakhar/simple-hangman.git
```

### 2. Navigate to the project directory:

```bash
cd simple-hangman
```
### 3. Run the game:

```bash
python main.py
```

### 4. Usage
- When the game starts, you will see the logo and a word with blanks representing letters to guess.
- You will be prompted to enter a letter. 
- The game will check if the letter is in the word and update the display accordingly.
- Each incorrect guess will result in the loss of a life and will update the hangman figure.
- The game continues until you either guess the word correctly or run out of lives.
- The final message will show if you won or lost and reveal the word.

### 5. Project Structure
```bash
simple-hangman/
├── main.py            # Main game logic
├── hangman_art.py     # Art for the hangman stages and logo
├── hangman_words.py   # Word list for the game
└── README.md          # Project documentation
```

### 6. Technologies Used
- Python 3.x

### 7. A short demo:

```bash
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    
****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: ______a__

  +---+
  |   |
      |
      |
      |
      |
=========

****************************6/6 LIVES LEFT****************************
Guess a letter: e
Word to guess: ______a_e

  +---+
  |   |
      |
      |
      |
      |
=========

****************************6/6 LIVES LEFT****************************
Guess a letter: i
Word to guess: _i____a_e

  +---+
  |   |
      |
      |
      |
      |
=========

****************************6/6 LIVES LEFT****************************
Guess a letter: o
Word to guess: _i__o_a_e

  +---+
  |   |
      |
      |
      |
      |
=========

****************************6/6 LIVES LEFT****************************
Guess a letter: u
You guessed u, that's not in the word. You lose a life.
Word to guess: _i__o_a_e

  +---+
  |   |
  O   |
      |
      |
      |
=========

****************************5/6 LIVES LEFT****************************
Guess a letter: l
You guessed l, that's not in the word. You lose a life.
Word to guess: _i__o_a_e

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************4/6 LIVES LEFT****************************
Guess a letter: a
You have already guessed a
****************************4/6 LIVES LEFT****************************
Guess a letter: p
You guessed p, that's not in the word. You lose a life.
Word to guess: _i__o_a_e

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
****************************3/6 LIVES LEFT****************************
Guess a letter: t
You guessed t, that's not in the word. You lose a life.
Word to guess: _i__o_a_e

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

****************************2/6 LIVES LEFT****************************
Guess a letter: m
Word to guess: mi__o_a_e

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

****************************2/6 LIVES LEFT****************************
Guess a letter: n
You guessed n, that's not in the word. You lose a life.
Word to guess: mi__o_a_e

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

****************************1/6 LIVES LEFT****************************
Guess a letter: i
You have already guessed i
****************************1/6 LIVES LEFT****************************
Guess a letter: c
Word to guess: mic_o_a_e

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

****************************1/6 LIVES LEFT****************************
Guess a letter: e
You have already guessed e
****************************1/6 LIVES LEFT****************************
Guess a letter: r
Word to guess: micro_a_e

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

****************************1/6 LIVES LEFT****************************
Guess a letter: o
You have already guessed o
****************************1/6 LIVES LEFT****************************
Guess a letter: w
Word to guess: microwa_e

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

****************************1/6 LIVES LEFT****************************
Guess a letter: a
You have already guessed a
****************************1/6 LIVES LEFT****************************
Guess a letter: v
Word to guess: microwave
****************************YOU WIN****************************
```