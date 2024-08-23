from collections import defaultdict

from WordCounts import WordCounts
from WordsFactory import WordsFactory


class CountDefaultdict:
    """
    An example of counting the number of words using a defaultdict
    """
    def __init__(self, words_factory: WordsFactory):
        self.words_factory: WordsFactory = words_factory

    def word_counts(self) -> WordCounts:
        print("CountDefaultdict.word_counts()")
        word_counts = defaultdict(int)

        for word in self.words_factory.words():
            word_counts[word] += 1

        return WordCounts([(word, count) for word, count in word_counts.items()])
