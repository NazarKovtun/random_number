from Cached import Cached
from Count import Count
from Distinct import Distinct
from FirstLetter import FirstLetter
from Jack import Jack
from Lower import Lower
from StartsWith import StartsWith


class JackWordsOOP:
    """
    Practical use of the OOP
    """
    @staticmethod
    def print() -> None:
        print("-" * 20)
        print("JackWordsOOP.print()")
        jack = Jack()
        lower = Cached(Lower(jack))

        unique = Distinct(lower)
        first = FirstLetter(unique)

        letters = Count(first)
        letters.word_counts().print()

        start_with = StartsWith(lower, "m")
        words = Count(start_with)
        words.word_counts().print()
