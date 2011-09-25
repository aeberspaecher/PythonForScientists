cimport numpy as np # also C-import types

cpdef np.ndarray[double] sincSquareCython2\
    (np.ndarray[double] x):

    cdef int i
    cdef double pi = 3.1415926535897932384626433
    cdef np.ndarray[double] retVal = np.zeros_like(x)

    for i in range(len(x)):
        retVal[i] = pow(sin(pi*x[i]) / (pi*x[i]), 2)
