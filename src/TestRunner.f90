program main
	use assert_class
	use circle_class
	use test_class
	implicit none

	call setup
	call funit_assertions
	call teardown
	call setup
	call radius_is_stored_properly
	call teardown
	call setup
	call area_varies_with_radius
	call teardown
end program