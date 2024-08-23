from typing import Generator

from WordsFactory import WordsFactory


class DistinctWords(Generator[str, None, None]):
    def __init__(self, source: WordsFactory):
        self.source: Generator[str, None, None] = source.words()
        self.unique_words = set()

    def throw(self, __typ, __val=None, __tb=None):
        raise __typ

    def send(self, __value):
        for word in self.source:
            if word not in self.unique_words:
                self.unique_words.add(word)
                return word

        raise StopIteration


class DistinctGen(WordsFactory):
    def __init__(self, source: WordsFactory):
        self.source: WordsFactory = source

    def words(self) -> Generator[str, None, None]:
        return DistinctWords(self.source)


class Distinct(WordsFactory):
    def __init__(self, source: WordsFactory):
        self.source: WordsFactory = source

    def words(self) -> Generator[str, None, None]:
        print("Distinct.words()")
        unique_words = set()
        for word in self.source.words():
            if word not in unique_words:
                yield word
                unique_words.add(word)
