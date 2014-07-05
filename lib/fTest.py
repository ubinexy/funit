# -*- coding: utf-8 -*-  
import os
from compiler import *
from parse import *


class Test(object):

	_main = 'TestRunner'

	def __init__(self, opts):
		self.source = opts.src
		self.target = opts.target
		self._parse_and_compile()



	def _parse_and_compile(self):
		p = Parse(self.target) # fullpath
		p.write_to_target()

		C = Compiling(self.source) # fullpath 
		C.write_to_makefile()



	def run_test(self):
		os.system('make')
		print 20 * '='
		cmd = "./a.exe"# > a.OutputFile"
		# if os.path.exists('a.InputFile'):
			# cmd = "cat a.InputFile|" + cmd
		os.system(cmd)