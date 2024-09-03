from typing import Iterator

from Ns import Ns
from Rnd import Rnd


class NsFactory:
    """
    A random number factory that returns them as an Iterator
    """
    def __init__(self, r: Rnd, size: int = 21) -> None:
        self.r: Rnd = r
        self.size: int = size

    def ns(self) -> Ns:
        """
        :return: Ns object with generator
        """
        ns_generator: Iterator[int] = (self.r.next() for _ in range(self.size))
        return Ns(ns_generator)
