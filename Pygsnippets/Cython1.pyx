cdef extern from "math.h":
    double sin(double)
    double pow(double, int)

def sincSquareCython1(x):

    pi = 3.1415926535897932384626433
    retVal = np.zeros_like(x)

    for i in range(len(x)):
        retVal[i] = (sin(pi*x[i]) / (pi*x[i]))**2

    return retVal
