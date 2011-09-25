subroutine sincsquaref2py1(x, n, outVal)
    implicit none

    double precision, dimension(n), intent(in) :: x
    integer, intent(in) :: n
    double precision, dimension(n), intent(out) :: outVal
    double precision, parameter :: pi = 4.0d0 * atan(1.0d0)

    outVal(:) = (sin(pi*x(:)) / (pi*x(:)))**2

end subroutine sincsquaref2py1
