from collections import Counter

from WordCounts import WordCounts
from WordsFactory import WordsFactory


class Count:
    """
    An example of counting the number of words using a collections.Counter
    """
    def __init__(self, words_factory: WordsFactory):
        self.words_factory: WordsFactory = words_factory

    def word_counts(self) -> WordCounts:
        print("Count.word_counts()")
        word_counts = Counter(self.words_factory.words())
        return WordCounts(word_counts.most_common())
