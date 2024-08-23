from typing import Generator

from WordsFactory import WordsFactory


class FirstLetter(WordsFactory):
    def __init__(self, source: WordsFactory):
        self.source: WordsFactory = source

    def words(self) -> Generator[str, None, None]:
        """
        :return: first letter generator
        """
        print("FirstLetter.words()")
        words = self.source.words()
        for word in words:
            yield word[0]