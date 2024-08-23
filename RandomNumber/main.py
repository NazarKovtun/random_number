from Rnd09AZ import Rnd09AZ
from RndNAZ import RndNAZ
from Ns import Ns
from NsFactory import NsFactory
from Rnd import Rnd
from RndPseudo import RndPseudo
from RndReal import RndReal
from RndPython import RndPython
from RndInt import RndInt


def main() -> None:
    r2: Rnd = RndPython(1)
    # r: Rnd = RndPseudo()

    rnd = Rnd09AZ(1)
    ns_fac = NsFactory(rnd)
    ns = ns_fac.ns()
    ns.print()

    ns2_factory = NsFactory(r2)
    ns2 = ns2_factory.ns()
    ns2.print()

    # ns_factory = NsFactory(r)
    # ns = ns_factory.ns()
    # ns.print()


if __name__ == "__main__":
    main()
