# -*- coding: utf-8 -*-  
import sys, os, re
from compiler import *
from parse import *

class OptionError(Exception):
	pass

class Test(object):

	_main = 'TestRunner'

	def __init__(self, target):
		self.target = target
		m = re.match('([\s\S]*)(tests/)([^\.]+)(\.test)',target)
		try:
			if m == None:
				raise OptionError()
		except OptionError:
			print "Can't parse %s, try -h option for help!" % target
			sys.exit(2)

		
		self.source = m.group(1) + 'src/' + m.group(3) + '.f90'
		try:
			if os.path.exists(self.source):
				pass
			else:
				raise OptionError()
		except OptionError:
			print "Can't find %s, try -h option for help!" %self.source
			sys.exit(2)
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