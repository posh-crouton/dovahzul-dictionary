from bs4 import BeautifulSoup
import requests
from typing import List
from tqdm import tqdm


class ThuumIndexWord:
    def __init__(self, word: str, wordId: int):
        self.word = word
        self.wordId = wordId

    @staticmethod
    def get_words_from_initial(initial: str) -> List["ThuumIndexWord"]:
        html_content = requests.get(f"https://www.thuum.org/dictionary.php?letter={initial.upper()}").text
        soup = BeautifulSoup(html_content, "html.parser")
        elements = soup.find_all(name="a", class_="dic-word")

        output = []
        for element in elements:
            output.append(ThuumIndexWord(element.text, element.get("href").split("w=")[1]))
        return output

    @staticmethod
    def get_all_words() -> List["ThuumIndexWord"]:
        output = []
        for c in tqdm("abcdefghijklmnopqrstuvwxyz", desc="Indexing words on thuum.org"):
            output += ThuumIndexWord.get_words_from_initial(c)
        return output
