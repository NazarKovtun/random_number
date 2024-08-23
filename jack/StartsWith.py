from typing import Generator

from WordsFactory import WordsFactory


class StartsWith(WordsFactory):
    def __init__(self, words_factory: WordsFactory, start_let: str):
        self.words_factory: WordsFactory = words_factory
        self.start_let: str = start_let

    def words(self) -> Generator[str, None, None]:
        """
        :return: word generator of start with
        """
        print("StartsWith.word()")
        for word in self.words_factory.words():
            if word.startswith(self.start_let):
                yield word