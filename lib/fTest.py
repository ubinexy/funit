# -*- coding: utf-8 -*-  
import os, re
from compiler import *
from parse import *


class Test(object):

	_main = 'TestRunner'

	def __init__(self, target):
		self.target = target
		m = re.match('([\s\S]*)(tests/)([^\.]+)(\.test)',target)
		# Need to do:
		# raise exception 
		self.source = m.group(1) + 'src/' + m.group(3) + '.f90'
		self._parse_and_compile()



	def _parse_and_compile(self):
		p = Parse(self.target)
		p.write_to_target()

		C = Compiling(self.source) 
		C.write_to_makefile()



	def run_test(self):
		os.system('make')
		print 20 * '='
		cmd = "./a.exe"# > a.OutputFile"
		# if os.path.exists('a.InputFile'):
			# cmd = "cat a.InputFile|" + cmd
		os.system(cmd)