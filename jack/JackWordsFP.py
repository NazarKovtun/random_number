from functools import reduce
from itertools import tee
from typing import Generator, Callable


def jack(jack_txt_path: str) -> Generator[str, None, None]:
    print("Jack.words()")
    with open(jack_txt_path, "r") as jack:
        for line in jack:
            lines = line.split()
            for words in lines:
                yield words.strip(".")


def print_line(items: any) -> None:
    for item in items:
        print(item, end=" ")
    print()


def distinct() -> Callable[[str], bool]:
    # clause
    unique_words = set()

    def unique_word(word: str) -> bool:
        if word not in unique_words:
            unique_words.add(word)
            return True
        else:
            return False

    return unique_word


def count(acc: dict[str, int], x: str) -> dict[str, int]:
    acc[x] = acc.get(x, 0) + 1
    return acc


class JackWordsFP:
    """
    Practical use of the Functional Programming
    """

    @staticmethod
    def print() -> None:
        print("-" * 20)
        print("JackWordsFP.print()")

        words0 = jack("jack.txt")
        words1 = map(lambda x: x.lower(), words0)

        words2, m_words0 = tee(words1)

        words3 = filter(distinct(), words2)
        words4 = map(lambda x: x[0], words3)
        words5 = reduce(count, words4, {})
        words6 = sorted(words5.items(), key=lambda x: -x[1])
        print_line(words6)

        m_words1 = filter(lambda x: x[0] == "m", m_words0)
        m_words2 = reduce(count, m_words1, {})
        m_words3 = sorted(m_words2.items(), key=lambda x: -x[1])

        print_line(m_words3)
