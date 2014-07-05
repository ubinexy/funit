# -*- coding: utf-8 -*-
from argparse import ArgumentParser

class Options(object):
	
	def __init__(self):
		self._init_parser()


	def _init_parser(self):
		usage = 'bin/funit (-t foo.test)'
		self.parser = ArgumentParser(usage=usage)
		
		# self.parser.add_argument('-s',
		# 						'--src',
		# 						dest='src',
		# 						help='specify source destination')

		self.parser.add_argument('-t',
								dest='target',
								help='specify foo.test path')


	def parse(self, opts):
		return self.parser.parse_args(opts)
		