module test_circle_class
	use circle_class
	use assert_class
	implicit none
	real, parameter :: radius = 1.5d0
	real, parameter :: pi = 3.14159d0
	type(circle) :: c

contains

	setup
		c = circle(radius)
	end setup

	teardown

	end teardown


	test funit_assertions
		call assert_real_equal(0.999999999e0, 1.0e0)
		call assert_equal_within(1e-7, 0.0, 1e-6)
		call assert_equal(1, 5 - 4)
		call assert_true(4 == 4)
	end test

	test radius_is_stored_properly
		call assert_real_equal(radius, 1.5d0)
	end test

	test area_varies_with_radius
		real :: area
		area = circle_area(c)
		assert_equal_within(area, pi*(radius**2), 1e-3)
	end test

end module