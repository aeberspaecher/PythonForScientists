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
  integer, dimension(8) :: time1, time2
  integer :: j

  x(:) = 0.25d0

  call date_and_time(values=time1)
  
  do j=1,50
    x(:) = sincSquare(x(:))
  end do
  
  call date_and_time(values=time2)

  print *, time2-time1

end program sinc
