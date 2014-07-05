# -*- coding: utf-8 -*-  
import sys
from lib.options import Options
from lib.fTest import Test 

if __name__ == '__main__':
	opts = Options().parse(sys.argv[1:])

	t = Test(opts)
	t.run_test()