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
    rnd: Rnd = RndReal()
    
    ns_factory = NsFactory(rnd)
    ns = ns_factory.ns()
    ns.print()
    
    # rnd = Rnd09AZ(1)
    # ns_fac = NsFactory(rnd)
    # ns = ns_fac.ns()
    # ns.print()


if __name__ == "__main__":
    main()
