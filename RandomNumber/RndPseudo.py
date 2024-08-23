import time
import Rnd


class RndPseudo(Rnd.Rnd):
    def __init__(self, seed: int = None) -> None:
        self.seed = time.perf_counter_ns() if seed is None else seed
        self.a = 25214903917
        self.c = 11
        self.m = 0x1_0000_0000_0000  # 2^48

    @property
    def next(self) -> int:
        """
        :return: random number using a pseudo-random method
        """
        self.seed = (self.seed * self.a + self.c) % self.m
        return (self.seed >> 16) & Rnd.MASK31
