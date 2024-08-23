class WordCounts:
    """
    Used to display the slugs in the console
    """
    def __init__(self, word_counts: list[(str, int)]):
        self.word_counts: list[(str, int)] = word_counts

    def print(self):
        self.__print(self.word_counts)

    def print_sorted_by_count_desc(self):
        word_counts = sorted(self.word_counts, key=lambda x: -x[1])
        self.__print(word_counts)

    @staticmethod
    def __print(word_counts: list[(str, int)]):
        for word_count in word_counts:
            print(word_count, end=" ")
        print()
