import numpy as np
from math import sin, pi

def sincSquare(x):
    """Return the sinc(x) = (sin(x)/x)**2 of the array
    argument x.
    """
    retVal = np.zeros_like(x)
    for i in range(len(x)):
        retVal[i] = (sin(pi*x[i]) / (pi*x[i]))**2

    return retVal
