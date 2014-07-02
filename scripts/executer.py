# -*- coding: utf-8 -*-  
import os
from compiler import *
from render import *

TEST_DIR = '/Users/shiqi/Projects/funit/tests/'
main = 'TestRunner'



def execute(name):
	if os.path.exists('a.InputFile'):
		cmd = "cat a.InputFile | ./a.exe > a.OutputFile"
	else:
		cmd = "./a.exe > a.OutputFile"
	os.system(cmd)
	print 'hi'



for file in os.listdir(TEST_DIR):
	name, suffix = os.path.splitext(file)

	if suffix == '.test':
		C = Rendering('circle_class', 'circle_class_test')
		C.write_to_target()

		C = Compiling('circle_class', 'circle_class_test')
		C.write_to_makefile()
		os.system('make')
		os.system('make clean')
		execute(name)
	else:
		pass