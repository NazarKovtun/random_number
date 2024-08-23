from abc import ABC, abstractmethod

MASK31: int = 0x7FFF_FFFF


class Rnd(ABC):
    @abstractmethod
    def next(self) -> int:
        """
        :return: number from [0, 2^31).
        """
        pass
