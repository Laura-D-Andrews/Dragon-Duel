import sys
import random


def play_game(filename):
    with open(filename) as file:
        word_list = file.read().split()

    one_dragon_list = []
    two_dragon_list = []
    army_dragons_list = []
    list_to_randomize = []
    blank_list = []
    level = ""

    for word in word_list:
        if len(word) <= 6:
            one_dragon_list.append(word)
        if len(word) > 7 and len(word) <= 8:
            two_dragon_list.append(word)
        if len(word) >= 9:
            army_dragons_list.append(word)

    print("Guess The Mystery Word")
    print("Mission: Protect the city from a scary dragon by correctly guessing each letter in the mystery word")
    print("Rules:")
    print('1. You have 8 lives \u2665')
    print('2. You only lose a life if you guess a letter incorrectly')

    start_answer = input(
        "Will you accept this mission? Type Y or N: ")
    if start_answer == "Y":
        print("\n")
        print("**Great! The city needs you. Lets play.**")
        print("\n")
    elif start_answer == "N" or start_answer != "Y":
        print("**You must not be the hero the city needs. Come back when you have enough courage.**")
        sys.exit()

    print("How difficult do you want this battle to be?")
    print("Choose to fight 1 dragon, 2 dragons, or an army of dragons.")

    level = input("Type 1, 2, or army: ")
    if level == "1":
        list_to_randomize = one_dragon_list
    elif level == "2":
        list_to_randomize = two_dragon_list
    elif level == "army":
        list_to_randomize = army_dragons_list

    word_random = random.choice(list_to_randomize)

    print(word_random)

    for letter in word_random:
        blank_list.append('_')
    print("The mystery word is: " + " ".join(blank_list))

    guesses = 3
    while guesses > 0:

        letter = input("guess a letter: ")
        if letter in word_random:
            print("correct")
            for index in range(len(word_random)):
                if word_random[index] == letter:
                    blank_list[index] = letter
            print(' '.join(blank_list))
            if '_' not in blank_list:
                print("you saved the city!")
                break

        elif letter not in word_random:
            guesses -= 1
            print("Incorrect. You have " + str(guesses) +
                  ' ' + "lives " + "\u2665 "  "left.")
            if guesses == 0:
                print("\n")
                print(
                    "*** GAME OVER. The word was " + word_random.upper() + ". The scary dragons win ***")
                print("\n")

    play_game(filename)


if __name__ == "__main__":
    play_game("words.txt")
