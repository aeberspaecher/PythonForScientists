import numpy as np
from math import sin, pi

def sincSquare(x):
    """Return the sinc(x) = (sin(x)/x)**2 of the array
    argument x.
    """

    ret = np.zeros_like(x)
    for i in range(len(x)):
        ret[i] = (sin(pi*x[i]) / (pi*x[i]))**2

    return ret
