from typing import Generator

from WordsFactory import WordsFactory


class Cached(WordsFactory):
    """
    Saves file contents to the cache
    """
    def __init__(self, words_factory: WordsFactory):
        self.words_factory: WordsFactory = words_factory
        self.cach = []

    def words(self) -> Generator[str, None, None]:
        if self.cach:
            print("Cached.words() in cach")
            for word in self.cach:
                yield word
        else:
            print("Cached.words() not in cach")
            for word in self.words_factory.words():
                self.cach.append(word)
                yield word
