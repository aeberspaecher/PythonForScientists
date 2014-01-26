! compile with
! f2py -lgomp -c sinc_square_f2py.f90 --f90flags="-fopenmp" -m sinc_square_f2py

subroutine sinc_square_f2py1(x, n, out_vals)
    implicit none

    double precision, dimension(n), intent(in) :: x
    integer, intent(in) :: n
    double precision, dimension(n), intent(out) :: out_vals
    double precision, parameter :: pi = 4.0d0 * atan(1.0d0)

    out_vals(:) = (sin(pi*x(:)) / (pi*x(:)))**2
end subroutine sinc_square_f2py1

! set number of OpenMP threads:
subroutine set_num_threads(n)
    use omp_lib
    implicit none

    integer, intent(in) :: n

    call OMP_set_num_threads(n)
end subroutine set_num_threads

! OpenMP variant of sincSquare:
subroutine sinc_square_f2py2(x, n, out_vals)
    implicit none

    double precision, dimension(n), intent(in) :: x
    integer, intent(in) :: n
    double precision, dimension(n), intent(out) :: out_vals

    integer :: i
    double precision, parameter :: pi = 4.0d0 * atan(1.0d0)

    !$OMP PARALLEL DO SHARED(x, out_vals)
    do i = 1, n
        out_vals(i) = (sin(pi*x(i)) / (pi*x(i)))**2
    end do
    !$OMP END PARALLEL DO
end subroutine sinc_square_f2py2
