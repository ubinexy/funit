# -*- coding: utf-8 -*-  
import os

class Compiling(object):
	
	def __init__(self, arg1, arg2):
		self.arg1 = arg1
		self.arg2 = arg2
		self.target = open('makefile', 'w')



	def __del__(self):
		self.target.close()


	def write_to_makefile(self):
		self.target.write ('FC = gfortran\n')
		self.target.write ('FLAGS = -g -WALL\n')
		self.target.write ('\n')
		self.target.write ('OBJ = *.o\n')
		self.target.write ('MOD = *.mod\n')
		self.target.write ('\n')
		self.target.write ('a.exe: %s.f90 $(OBJ)\n' % self.arg1)
		self.target.write ('\t$(FC) $(FLAGS) $(OBJ) %s.f90 -o a.exe\n' % self.arg1)
		self.target.write ('\n')
		self.target.write ('%s.o: %s.f90\n' % (self.arg2, self.arg2))
		self.target.write ('\t$(FC) -c %s.f90\n' % self.arg2)
		self.target.write ('\n')
		self.target.write ('assert_class.o: assert_class.f90\n')
		self.target.write ('\t$(FC) -c assert_class.f90\n')
		self.target.write ('\n')
		self.target.write ('clean:\n')
		self.target.write ('\trm -f $(OBJ) $(MOD)\n')



	def compile_makefile(self):
		os.system('make')
		os.system('make clean')



arg1 = 'main'
arg2 = 'test_class'
c = Compiling(arg1, arg2)
c.write_to_makefile()
c.compile_makefile()