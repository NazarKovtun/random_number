"""
You can use:
- RndReal;
- RndPython;
- RndPseudo;
- RndInt;
- RndNAZ;
- Rnd09AZ.
"""
from RndReal import RndReal
from NsFactory import NsFactory
from Ns import Ns


def main() -> None:
    rnd = RndReal()
    ns_factory = NsFactory(rnd)
    ns = ns_factory.ns()
    ns.print()


if __name__ == "__main__":
    main()
