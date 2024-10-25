# Random Number
## Description
These are examples of random number generation algorithms from 0 to 2^31 using OOP (encapsulation, abstraction, polymorphism and inheritance).

## What's inside
This program uses several algorithms for generating random numbers, namely:
- `RndReal` - uses system time in nanoseconds;
- `RndPseudo` - uses mathematical formula to determine a random number;
- `RndPython` - uses the build-in Python ramdom module;
- `RndInt` - returns random number from 111 to 999 using any Random generator;
- `RndNAZ` - returns one char from A-Z using Ascii Unicode;
- `Rnd09AZ` - returns one char from 09-AZ using Ascii Unicode.

Other files that are important for the program to work:
- `Rnd` - abstract class from which other generators inherit;
- `Ns` - outputs characters to the console using Iterator;
- `NsFactory` - random number factory that returns them as an Iterator;

## How it works
In module `main.py` initialize the generator (`Rnd`), pass it to the factory (`NsFactory`), and then to the object for output to the console (`Ns`), from which we call the `print()` method.

`main.py`
```python
from RndReal import RndReal
from NsFactory import NsFactory
from Ns import Ns

def main():
    rnd = RndReal()
    ns_factory = NsFactory(rnd)
    ns = ns_factory.ns()
    ns.print()

if __name__ = '__main__':
	main()
```

**If you want use `RndInt`, `RndNAZ` or `Rnd09AZ` you need write**:

`main.py`
```python
from Rnd09AZ import Rnd09AZ  # or RndInt or RndNAZ
from NsFactory import NsFactory
from Ns import Ns

def main():
    rnd = Rnd09AZ(1)
    ns_factory = NsFactory(rnd)
    ns = ns_factory.ns()
    ns.print()

if __name__ = '__main__':
	main()
```
You need to specify `seed` in `Rnd09AZ`.
