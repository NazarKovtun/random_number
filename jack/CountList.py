from typing import Generator

from Jack import Jack
from WordCounts import WordCounts
from WordsFactory import WordsFactory


class CountList:
    """
    An example of counting the number of words using a list
    """
    def __init__(self, words_factory: WordsFactory):
        self.words_factory: WordsFactory = words_factory

    def word_counts(self) -> WordCounts:
        print("CountList.word_counts()")
        word_counts: list[(str, int)] = []

        for word in self.words_factory.words():
            not_found = True
            i = 0

            while i < len(word_counts):
                word_count = word_counts[i]
                if word_count[0] == word:
                    word_counts[i] = (word_count[0], word_count[1] + 1)
                    not_found = False
                    break
                i += 1

            if not_found:
                word_counts.append((word, 1))

        return WordCounts(word_counts)