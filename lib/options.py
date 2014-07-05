# -*- coding: utf-8 -*-
from argparse import ArgumentParser

class Options(object):
	
	def __init__(self):
		self._init_parser()


	def _init_parser(self):
		usage = 'bin/project [选项] file'
		self.parser = ArgumentParser(usage=usage)
		
		self.parser.add_argument(	'-s',
									'--src',
									dest='src',
									help='source destination')

		self.parser.add_argument(	'-t',
									'--target',
									dest='target',
									help='target destination')



	def parse(self, opts):
		print self.parser.parse_args(opts)
		