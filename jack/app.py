from JackWordsFP import JackWordsFP
from JackWordsIP import JackWordsIP
from JackWordsOOP import JackWordsOOP
from WorkTime import WorkTime


def main():
    ip = WorkTime("IP", JackWordsIP.print)
    oop = WorkTime("OOP", JackWordsOOP.print)
    fp = WorkTime("FP", JackWordsFP.print)

    ip.performance()
    oop.performance()
    fp.performance()

    ip.print()
    oop.print()
    fp.print()

    min_wt = ip.min(oop.min(fp))

    ip.print_diff(min_wt)
    oop.print_diff(min_wt)
    fp.print_diff(min_wt)


if __name__ == "__main__":
    main()
