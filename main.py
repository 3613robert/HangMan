import random
from hangman import HANGMAN
import pandas as pd
from github import Github

def generate_word():
    data = pd.read_csv('words.csv', header=None)
    words_row = data.iloc[1]
    random_word = random.choice(words_row)
    return random_word

def valid_input(guess):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return len(guess) == 1 and guess.lower() in alphabet

def play_again():
    global game_on
    play = input('Do you want to play again? type: y/n \n')
    if play == 'y':
        game(random_word=generate_word())
    elif play == 'n':
        game_on = False

def game(random_word):
    wrong_guess = 0
    r_word_list = []
    guessed_letters = []
    for _ in random_word:
        r_word_list.append("_")
    print(r_word_list)
    while game_on:
        try:
            guess = input("What letter will you guess?: \n")
            if not valid_input(guess):
                print('Please enter a single valid letter')
                continue
            if guess in guessed_letters:
                print("You've already guessed that letter! Try another letter")
            else:
                guessed_letters.append(guess)
                for i in range(len(random_word)):
                    if guess in random_word:
                        if guess == random_word[i]:
                            r_word_list[i] = guess
                joined_word = ' '.join(r_word_list)
                print(joined_word)
                if guess not in random_word:
                    print(HANGMAN[wrong_guess])
                    wrong_guess += 1
                    joined_word = ' '.join(r_word_list)
                    print(joined_word)
                if wrong_guess == len(HANGMAN):
                    print(f"You've lost!\nThe word was: {random_word}")
                    play_again()
                if '_' not in r_word_list:
                    print("You've guessed the word!")
                    play_again()
        except ValueError:
            print("Please enter a valid letter")

game_on = True

game(random_word=generate_word())