from typing import Generator

from WordsFactory import WordsFactory


class Jack(WordsFactory):
    """
    Word factory that takes values from a file
    """
    def __init__(self):
        self.path = "jack.txt"

    def words(self) -> Generator[str, None, None]:
        print("Jack.words()")
        with open(self.path, "r") as jack:
            for line in jack:
                lines = line.split()
                for words in lines:
                    yield words.strip(".")
