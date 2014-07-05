# -*- coding: utf-8 -*-  
import sys, os
from lib.options import Options
from lib.fTest import Test 


def _ergodic():
	_test_dir = os.getcwd() + '/tests/'
	for file in os.listdir(_test_dir) :
		if os.path.splitext(file)[1] == '.test' :
			test = Test(_test_dir + file)
			test.run_test()



if __name__ == '__main__':

	argv = sys.argv[1:]
	
	if len(argv) == 0:
		_ergodic()
	elif len(argv) == 1:
		optparse = Options().parse(argv)
	elif len(argv) == 2:
		optparse = Options().parse(argv)
		test = Test(optparse.target)
		test.run_test()
	else:
		sys.exit(2) 
