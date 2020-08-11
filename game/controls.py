from random import choice
from sys import exit


def generate_random_words(words: list):
    """Functions that pick a random element in a list"""
    return choice(words).lower()


def read_words():
    """Function that read the words from a file and save them on a list"""
    filename = 'game/words.txt'
    try:
        with open(filename) as f:
            words = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("File Not Found")
        exit()
    else:
        return words
