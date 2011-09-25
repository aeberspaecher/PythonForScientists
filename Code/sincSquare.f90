function sincSquare(x)
  double precision, dimension(:), intent(in) :: x
  double precision, dimension(size(x)) :: sincSquare

  double precision, parameter :: pi = 4.0d0*atan(1.0d0)

  sincSquare(:) = (sin(pi*x)/(pi*x))**2

end function sincSquare


program sinc

    interface
        function sincSquare(x)
    double precision, dimension(:), intent(in) :: x
    double precision, dimension(size(x)) :: sincSquare
    end function sincSquare

    end interface

    double precision, dimension(1000000) :: x

    x(:) = 1.0d0

    x(:) = sincSquare(x(:))

end program sinc
