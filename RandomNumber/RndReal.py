import time
import Rnd


class RndReal(Rnd.Rnd):
    def __init__(self, seed: int = None) -> None:
        self.seed = time.perf_counter_ns() if seed is None else seed

    def next(self) -> int:
        """
        :return: random number using a real-random method
        """
        self.seed = self.seed ^ time.perf_counter_ns()
        return self.seed % Rnd.MASK31
