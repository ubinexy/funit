module assert_class
    implicit none
    integer, save :: count = 0
    public :: count, assert_real_equal, assert_equal, assert_equal_with, assert_true, assert_array

contains

    subroutine assert_equal(actual, expect)
        implicit none
        integer :: actual, expect
        if(actual .ne. expect) then 
            print *, 'assert_equal() fail'
        else
            count = count + 1 
        end if
    end subroutine


    subroutine assert_real_equal(actual, expect)
        implicit none
        real :: actual, expect
        if(actual .ne. expect) then 
            print *, 'assert_real_equal() fail'
        else
            count = count + 1
        end if
    end subroutine

    subroutine assert_true(actual)
        logical :: actual
        if(actual .neqv. .TRUE.) then
            print *, 'assert_ture() fail'
        else
            count = count + 1
        end if
    end subroutine

    subroutine assert_equal_with(actual, expect, tor)
        real :: actual, expect, tor
        real :: error
        error = abs(actual-expect)
        if( error .ge. tor) then
            print *, 'assert_equal_with() fail'
        else
            count = count + 1
        end if
    end subroutine

    subroutine assert_array(actual, expect)
        real, dimension(*) :: actual, expect
        real :: element
        ! unfinished   
    end subroutine

end module