# -*- coding: utf-8 -*-  
import os
from Compile import *
from Parse import *


class test(object):

	_main = 'TestRunner'

	def __init__(self, opts):
		self.source = opts.src
		self.target = opts.target
		self.init_parse_and_compile()



	def _init_parse_and_compile(self):
		p = Parse(self.target)
		p.write_to_target()

		C = Compiling(self.source, '.test.f90')
		C.write_to_makefile()



	def run_test(self):
		cmd = "./a.exe > a.OutputFile"
		if os.path.exists('a.InputFile'):
			cmd += "cat a.InputFile"	
		os.system(cmd)