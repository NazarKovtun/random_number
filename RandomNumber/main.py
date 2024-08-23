"""
You can use:
- RndReal;
- RndPython;
- RndPseudo;
- RndInt;
- RndNAZ;
- Rnd09AZ.
"""
from RndPseudo import RndPseudo
from NsFactory import NsFactory
from Ns import Ns


def main() -> None:
    rnd = RndPseudo()
    ns_factory = NsFactory(rnd)
    ns = ns_factory.ns()
    ns.print()


if __name__ == "__main__":
    main()
