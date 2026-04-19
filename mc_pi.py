from random import random as u01
pi = lambda n: 4 * sum(abs(u01() + 1j * u01()) < 1 for _ in range(n)) / n
