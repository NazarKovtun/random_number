from typing import Iterator


class Ns:
    """
    An object that outputs characters
    to the console using Iterator
    """
    def __init__(self, ns: Iterator[int]) -> None:
        self.ns: list[int] = list(ns)

    def print(self) -> None:
        for n in self.ns:
            print(n, end=' ')
        print()
