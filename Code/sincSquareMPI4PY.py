from mpi4py import MPI
import numpy as np
from math import sin
from matplotlib.pyplot import *

def sincSquareMPI(x):
    """Return the sinc(x) = (sin(x)/x)**2 of the array argument x.
    """

    # assume the array length can be divided by the number of processes
    
    retVal = np.zeros_like(x)
    tempVals = np.zeros_like(x)

    # find min and max index for each process:
    lowerIndex = 0 + len(x) * MPIrank/MPIsize
    upperIndex = len(x) * (MPIrank+1)/MPIsize

    print("Process %s having indices (%s, %s)"%(MPIrank, lowerIndex, upperIndex))
    
    for i in range(lowerIndex, upperIndex):
        tempVals[i] = (sin(np.pi*x[i]) / (np.pi*x[i]))**2

    MPIcomm.Reduce(tempVals, retVal, op=MPI.SUM, root=MPIroot)

    return retVal

MPIroot = 0 # define the root process
MPIcomm = MPI.COMM_WORLD # MPI communicator

# get rank (= number of individual process) and
# size (= total number of processes)
MPIrank, MPIsize = MPIcomm.Get_rank(), MPIcomm.Get_size()

x = np.linspace(-5,+5,10000,endpoint=True)
y = sincSquareMPI(x)

if(MPIrank == 0):
    plot(x,y)
    show()

