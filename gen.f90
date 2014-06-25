program main
    use a_class
    implicit none
    integer :: a
    real(8) :: b
    
	setup
    ! Place code here that should run before each test
    	simple sdf
    	coasd here 
    	you see 
    end setup

    teardown

    assert_equal(1, 5, 4)
    

    ! This code runs immediately after each test
    

end program
