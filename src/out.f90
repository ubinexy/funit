program main
	!use circle_class
	!use assert_class
	implicit none
	real, parameter :: radius = 1.5d0
	real, parameter :: pi = 3.14159d0
	!type(circle) :: c

	!	c = circle(radius)

	subroutine funit_assertions
	!	call assert_real_equal(0.999999999e0, 1.0e0)
	!	call assert_equal_within(1e-7, 0.0, 1e-6)
	!	call assert_equal(1, 5 - 4)
	!	call assert_true(4 == 4)
	end subroutine
	call funit_assertions


end program
