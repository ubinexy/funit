from nose.tools import *
from lib.parse import *


def test_init():
	Test_Path = "/Users/shiqi/Projects/funit/src/circle_class.test"
	P = Parse(Test_Path)
	assert_equal(P.ripe , Test_Path +'.f90')
	P.write_to_target()

# TestRunner.f90
# '''
# program main
# 	use circle_class_test
# 	implicit none
# 	call setup
# 	call funit_assertions
# 	call teardown
# 	call setup
# 	call radius_is_stored_properly
# 	call teardown
# 	call setup
# 	call area_varies_with_radius
# 	call teardown
# end program
# '''


