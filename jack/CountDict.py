from WordCounts import WordCounts
from WordsFactory import WordsFactory


class CountDict:
    """
    An example of counting the number of words using a dict
    """
    def __init__(self, words_factory: WordsFactory):
        self.words_factory: WordsFactory = words_factory

    def word_counts(self) -> WordCounts:
        print("CountDict.word_counts()")
        word_counts: dict[str, int] = {}

        for word in self.words_factory.words():
            word_counts[word] = word_counts.get(word, 0) + 1

        return WordCounts([(word, count) for word, count in word_counts.items()])
