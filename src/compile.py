# -*- coding: utf-8 -*-  
import os

class Make(object):
	
	def __init__(self):
		self.arg1 = 'main'
		self.arg2 = 'test_class'
		self.target = open('makefile', 'r+')

	def __del__(self):
		self.target.close()

	def content(self):
		text = '''
FC = gfortran
FLAGS = -g -WALL

OBJ = *.o
MOD = *.mod

a.exe: %s.f90 $(OBJ)
	$(FC) $(FLAGS) $(OBJ) %s.f90 -o a.exe

%s.o: %s.f90
	$(FC) -c %s.f90

assert_class.o: assert_class.f90
	$(FC) -c assert_class.f90

clean:
	rm -f $(OBJ) $(MOD)
	''' % (self.arg1, self.arg1, self.arg2, self.arg2, self.arg2) 

		print text
		self.target.write(text)


	def make(self):

		os.system('make')
		os.system('make clean')

