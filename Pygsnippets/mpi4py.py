from mpi4py import MPI

MPIroot = 0  # define the root process
MPIcomm = MPI.COMM_WORLD  # MPI communicator

MPIrank, MPIsize = MPIcomm.Get_rank(), MPIcomm.Get_size()

...

MPIcomm.Reduce(tempVals, retVal, op=MPI.SUM, root=MPIroot)
