from math import pi
from sys import argv

if len(argv) < 2:
    print('No radius passed. Exiting')
else:
    r = float(argv[1])
    print(2 * pi * r)
