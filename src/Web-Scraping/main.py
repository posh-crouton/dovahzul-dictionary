from thuum_scraper import *


def main():
    for word in ThuumIndexWord.get_all_words():
        print(word.word, word.wordId)


if __name__ == "__main__":
    main()
