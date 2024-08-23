from typing import Generator

from WordsFactory import WordsFactory


class Lower(WordsFactory):
    def __init__(self, source: WordsFactory):
        self.source = source

    def words(self) -> Generator[str, None, None]:
        """
        :return: lower words generator
        """
        print("Lower.word()")
        words = self.source.words()
        for word in words:
            yield word.lower()
