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

for file in os.listdir(TEST_DIR):
	name, suffix = os.path.splitext(file)

	if suffix == '.fun':
		print 'yes'
		C = Rendering(name, main)
		C.write_to_target()
		C = Compiling(main, name)
		C.write_to_makefile()
		C.compile_makefile()
		execute(name)
	else:
		pass