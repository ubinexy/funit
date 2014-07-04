# -*- coding: utf-8 -*-  
from nose.tools import *
from lib.compiler import Compiling

def test_compiling():
	Test_Path = "/Users/shiqi/Projects/funit/src/circle_class.f90"

	C = Compiling(Test_Path)
	C.write_to_makefile()
	# print C.src
	# print C.p



