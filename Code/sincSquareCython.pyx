#cython: boundscheck=False
#cython: cdivision=True

# compile to .c file with
# cython -a sincSquareCython.pyx
# Inspect the .c and the .html file if you want to
# gcc -O2 -shared -fPIC -march=native  -I/usr/include/python2.6/ -I/usr/lib64/python2.6/site-packages/numpy/core/include/ -o sincSquareCython.so sincSquareCython.c
# maybe you need to change to paths in the command above

import numpy as np
cimport numpy as np # also C-import types

# use math functions from math.h as those are faster:
cdef extern from "math.h":
    double sin(double)
    double pow(double, int)

def sincSquareCython1(x):
    """Return the sinc(x) = (sin(x)/x)**2 of the array argument x.
    """

    pi = 3.1415926535897932384626433

    retVal = np.zeros_like(x)

    for i in range(len(x)):
        retVal[i] = (sin(pi*x[i]) / (pi*x[i]))**2

    return retVal

cpdef np.ndarray[double] sincSquareCython2(np.ndarray[double] x): # note: cpdef!
    """Return the sinc(x) = (sin(x)/x)**2 of the array argument x.
    """

    cdef int i
    cdef double pi = 3.1415926535897932384626433
    cdef np.ndarray[double] retVal = np.zeros_like(x)

    for i in range(len(x)):
        retVal[i] = pow(sin(pi*x[i]) / (pi*x[i]), 2)
