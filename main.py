from game.hangman import Hangman


def main():
    w = Hangman(7)
    while True:
        w.draw_word_scheme()
        w.check_char(input("Enter a char -> "))
        w.check_win()


if __name__ == "__main__":
    main()
