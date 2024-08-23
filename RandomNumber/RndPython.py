import random

import Rnd


class RndPython(Rnd.Rnd):
    def __init__(self, seed: int = None) -> None:
        self.python_random = random.Random(seed)

    @property
    def next(self) -> int:
        """
        :return: random number using the built-in Python module
        """
        return self.python_random.randint(0, Rnd.MASK31)
