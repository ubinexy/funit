# -*- coding: utf-8 -*-  
import sys
from lib import Option
from lib import Test

if __name__ = '__main__':
	o = Option()
	opts = o.prase(sys.argv[1:])

	t = Test(opts)
	t.run_test()