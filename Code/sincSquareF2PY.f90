! compile with
! f2py -lgomp -c sincSquareF2PY.f90 --f90flags="-fopenmp" -m sincSquareF2PY

subroutine sincsquaref2py1(x, n, outVal)
    implicit none

    double precision, dimension(n), intent(in) :: x
    integer, intent(in) :: n
    double precision, dimension(n), intent(out) :: outVal
    double precision, parameter :: pi = 4.0d0 * atan(1.0d0)

    outVal(:) = (sin(pi*x(:)) / (pi*x(:)))**2

end subroutine sincsquaref2py1

! set number of OpenMP threads:
subroutine setNumThreads(n)
    use omp_lib
    implicit none

    integer, intent(in) :: n

    call OMP_set_num_threads(n)
    
end subroutine setNumThreads

! OpenMP variant of sincSquare:
subroutine sincsquaref2py2(x, n, outVal)
    implicit none

    double precision, dimension(n), intent(in) :: x
    integer, intent(in) :: n
    double precision, dimension(n), intent(out) :: outVal

    integer :: i
    double precision, parameter :: pi = 4.0d0 * atan(1.0d0)
    
    !$OMP PARALLEL DO SHARED(x, outVal)
    do i = 1, n
        outVal(i) = (sin(pi*x(i)) / (pi*x(i)))**2
    end do
    !$OMP END PARALLEL DO

end subroutine sincsquaref2py2



    
