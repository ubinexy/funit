
module assert_class
    implicit none
    private 
    public :: assert_equal, assert_equal_with, assert_true, assert_array

contains

    subroutine assert_equal(actual, expect)
        real(8) :: actual, expect
        if(actual .ne. expect) then 
            print *, 'assert_equal() fail'
        end if
    end subroutine

    subroutine assert_true(actual)
        logical :: a
        if(actual .ne. .TRUE.) then
            print *, 'assert_ture() fail'
        end if
    end subroutine

    subroutine assert_equal_with(actual, expect, tor)
        real(8) :: actual, expect, tor
        real(8) :: error
        error = abs(actual-expect)
        if( error .ge. tor) then
            print *, 'assert_equal_with() fail'
        end if
    end subroutine

    subroutine assert_array(actual, expect)
        real(8), dimension(*) :: actual, expect
        real(8) :: element
        ! unfinished   
    end subroutine

end module