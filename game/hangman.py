import sys

from game.controls import generate_random_words, read_words


class Hangman:
    """A class that represents the hangman game"""

    def __init__(self, attempts):
        """Initialize attributes"""
        self.attempts = attempts
        self.errors = 0
        self.word = generate_random_words(read_words())
        self.word2 = [" " if c == " " else "_" for c in self.word]

    def draw_scheme_world(self):
        """Draw the word scheme"""
        print("".join(self.word2))

    def check_char(self, char):
        """Check if a letter is on the word"""
        while len(char) > 1:
            char = input("Enter only a char -> ")
        char = char.lower()
        if char in self.word:
            indexes = []
            tmp_word = list(self.word)
            while char in tmp_word:
                index = tmp_word.index(char)
                indexes.append(index)
                tmp_word[index] = ""
            for i in indexes:
                self.word2[i] = char
        else:
            self.errors += 1
            print(f"This char is already inserted or isn't in the word -> +1 Error {self.errors}/{self.attempts}")

    def check_win(self):
        """Check if player has won or lose"""
        if "".join(self.word) == "".join(self.word2) and self.errors < self.attempts:
            print(f"You won! Word: {''.join(self.word)}")
            self.play_again()
        elif self.errors == self.attempts:
            print(f"You lose!\nThe word was: {''.join(self.word)}")
            self.play_again()

    def play_again(self):
        """Method that let you decide if you continue to play or not"""
        again = input("Do you want play again? (Y/n) -> ").lower()
        while again not in ('y', "n"):
            print("? I do not understand what you wrote")
            again = input("Do you want play again? (Y/n) -> ").lower()
        if again == 'y':
            self.__init__(self.attempts)
        else:
            print("Bye!")
            sys.exit()
