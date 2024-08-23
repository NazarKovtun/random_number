from statistics import mean, stdev
from typing import Callable

from StopWatch import StopWatch


class WorkTime:
    """
    Used to determine the time difference between the execution of two objects
    """
    def __init__(self, label: str, fn: Callable):
        self.__label: str = label
        self.__fn: Callable = fn
        self.__t_avg_s: float = 0.0
        self.__t_stde_s: float = 0.0
        self.__warm_up_count: int = 100
        self.__performance_count: int = 10000

    def performance(self):
        for _ in range(self.__warm_up_count):
            self.__fn()

        w_t = StopWatch()
        w_t_s = []
        for _ in range(self.__performance_count):
            w_t.restart()
            self.__fn()
            w_t.stop()
            w_t_s.append(w_t.total_seconds())

        self.__t_avg_s = mean(w_t_s)
        self.__t_stde_s = stdev(w_t_s)

    def print(self):
        error_p = self.__t_stde_s / self.__t_avg_s * 100.0
        print(f"{self.__label:<20} ({self.__t_avg_s:.6f}+-{self.__t_stde_s:.6f}) sec, {error_p:.1f}%")

    def min(self, right: "WorkTime") -> "WorkTime":
        return self if self.__t_avg_s <= right.__t_avg_s else right

    def print_diff(self, wt_100_p: "WorkTime"):
        diff = abs(self.__t_avg_s - wt_100_p.__t_avg_s)
        diff_p = diff / wt_100_p.__t_avg_s * 100.0

        print(f"{self.__label:<3} / {wt_100_p.__label} = {diff:.6f} sec, {diff_p:.1f}%")