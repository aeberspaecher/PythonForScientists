import numpy as np

def sincSquareNumPy1(x):

    return (np.sin(np.pi*x[:])/(np.pi*x[:]))**2

def sincSquareNumPy2(x):

    return np.sinc(x[:])**2
