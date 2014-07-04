# -*- coding: utf-8 -*-  
from nose.tools import *
from lib.options import Options

def test_lib():
	Opt = Options()
	assert_equal(	Opt.prase(['-s', 'source.f']).src,
				 	'source.f')
