module circle_class
	implicit none
	private
	public :: circle, circle_area

	real :: pi = 4.d0 * atan(1.d0)

	type circle
		real :: radius
	end type circle

contains
	
	function circle_area(this) result(area)
		type(circle), intent(in) :: this
		real :: area
		area = pi * this%radius**2
	end function circle_area

end module circle_class