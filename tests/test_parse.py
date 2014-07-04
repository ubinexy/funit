from nose.tools import *
from lib.parse import *

# def setup():

# @with_setup(setup)
def test_init():
	Test_Path = "/Users/shiqi/Projects/funit/src/circle_class.test"
	P = Parse(Test_Path)
	assert_equal(P.ripe , Test_Path +'.f90')
	assert_equal(P.footer(), 'end program')
	P.write_to_target()




