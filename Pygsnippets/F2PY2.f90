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
