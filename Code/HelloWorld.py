import sys
from math import sin, pi


def sincSquare(x):
    """Return sinc(x)^2.
    """
    if(x <> 0.0):
        return (sin(pi*x)/(pi*x))**2
    else:
        return 1.0


if(__name__ == '__main__'):
    x = sys.argv[1]
    y = sincSquare(float(x))
    print("sinc(%s)^2 = %s"%(x, y))
