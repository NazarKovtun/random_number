from typing import Final

import Rnd
from RndReal import RndReal

BEGIN: Final[int] = 111
END: Final[int] = 999
COUNT: Final[int] = END - BEGIN + 1


class RndInt(Rnd.Rnd):
    def __init__(self):
        self.rnd = RndReal()

    def next(self) -> int:
        """
        :return: random number
        """
        return BEGIN + (self.rnd.next() % COUNT)
