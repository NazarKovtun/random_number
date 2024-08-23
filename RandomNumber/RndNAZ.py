from typing import Final

import Rnd
from RndReal import RndReal

BEGIN: Final[int] = ord("A")
END: Final[int] = ord("Z")
COUNT: Final[int] = END - BEGIN + 1


class RndNAZ(Rnd.Rnd):
    def __init__(self, seed: int):
        self.rnd = RndReal(seed)

    @property
    def next(self) -> str:
        """
        :return: one char from AZ
        """
        return chr((self.rnd.next() % COUNT) + BEGIN)
