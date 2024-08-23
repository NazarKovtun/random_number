import time


class StopWatch:
    """
    Used to determine the time for which the program is executed
    """
    def __init__(self):
        self.__t_nc: int = time.perf_counter_ns()

    def restart(self):
        self.__t_nc: int = time.perf_counter_ns()

    def stop(self):
        self.__t_nc: int = time.perf_counter_ns() - self.__t_nc

    def total_seconds(self) -> float:
        return 1E-9 * self.__t_nc