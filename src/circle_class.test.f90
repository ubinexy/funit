module circle_class_test
	use circle_class
	use assert_class
	implicit none
	real, parameter :: radius = 1.5d0
	real, parameter :: pi = 3.14159d0
	type(circle) :: c

contains

	subroutine setup
		c = circle(radius)
	end subroutine

	subroutine teardown

	end subroutine


	subroutine funit_assertions
		call assert_real_equal(0.999999999e0, 1.0e0)
		call assert_equal_with(1e-7, 0.0, 1e-6)
		call assert_equal(1, 5 - 3)
		call assert_true(4 == 4)
	end subroutine

	subroutine radius_is_stored_properly
		call assert_real_equal(radius, 1.5e0)
	end subroutine

	subroutine area_varies_with_radius
		real :: area
		area = circle_area(c)
		call assert_equal_with(area, pi*(radius**2), 1e-3)
	end subroutine

end module