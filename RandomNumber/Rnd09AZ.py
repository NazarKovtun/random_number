from typing import Final

import Rnd
from RndReal import RndReal

BEGIN_NUM: Final[int] = ord("0")
END_NUM: Final[int] = ord("9")  # 0x39
END_NUM1: Final[int] = END_NUM + 1
BEGIN_LET: Final[int] = ord("A")  # 0x41
END_LET: Final[int] = ord("Z")
SHIFT_LET_NUM: Final[int] = BEGIN_LET - END_NUM
COUNT: Final[int] = END_LET - BEGIN_NUM + 1


class Rnd09AZ(Rnd.Rnd):
    def __init__(self, seed: int):
        self.rnd = RndReal(seed)

    @property
    def next(self) -> str:
        """
        :return: one char from 09-AZ
        """
        x1 = self.rnd.next() % COUNT + BEGIN_NUM
        x2 = x1 if not END_NUM < x1 < BEGIN_LET else x1 + SHIFT_LET_NUM
        return chr(x2)


