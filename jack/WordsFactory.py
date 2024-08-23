from abc import ABC, abstractmethod
from typing import Generator


class WordsFactory(ABC):
    @abstractmethod
    def words(self) -> Generator[str, None, None]:
        """
        :return: word from file
        """
        pass