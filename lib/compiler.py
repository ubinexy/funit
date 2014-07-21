# -*- coding: utf-8 -*-  
import os

class Compiling(object):
	'''
	# compile files 
	$(FC) -c $(PRO_DIR)/src/class.f90 
	$(FC) -c $(PRO_DIR)/src/assert_class.f90
	$(FC) -c $(PRO_DIR)/tests/class_test.f90
	$(FC) *.o TestRunner.f90
	'''



	def __init__(self, src):
		# self.src = src_name
		path,file=os.path.split(src)
		self.src = os.path.splitext(file)[0]
		# self.directory = os.path.split(path)[0]
		self.makefile = open('makefile', 'w')



	def __del__(self):
		self.makefile.close()


	def write_to_makefile(self):
		self.makefile.write ( 'FC = gfortran\n' )
		self.makefile.write ( 'FLAGS = -g\n' )
		self.makefile.write ( '\n' )
		self.makefile.write ( 'PRO_DIR = .\n' )
		self.makefile.write ( 'SRC_DIR = $(PRO_DIR)/src\n' )
		self.makefile.write ( 'TEST_DIR = $(PRO_DIR)/tests\n' )
		self.makefile.write ( '\n' )
		self.makefile.write ( 'OBJ = *.o\n' )
		self.makefile.write ( 'MOD = *.mod\n' )
		self.makefile.write ( '\n' )
		self.makefile.write ( 'a.exe: TestRunner.f90 test.o\n' )
		self.makefile.write ( '\t@$(FC) $(FLAGS) $(OBJ) TestRunner.f90 -o a.exe\n' )
		self.makefile.write ( '\n' )
		self.makefile.write ( 'test.o: $(TEST_DIR)/%s.test.f90 src.o assert_class.o\n' % self.src )
		self.makefile.write ( '\t@$(FC) -c $(TEST_DIR)/%s.test.f90\n' % self.src )
		self.makefile.write ( '\n' )
		self.makefile.write ( 'src.o: $(SRC_DIR)/%s.f90\n' % self.src )
		self.makefile.write ( '\t@$(FC) -c $(SRC_DIR)/%s.f90\n' % self.src )
		self.makefile.write	( '\t@echo \"COMPILING \'%s.f90\':\"\n' % self.src)
		self.makefile.write ( '\n' )
		self.makefile.write ( 'assert_class.o: $(SRC_DIR)/assert_class.f90\n' )
		self.makefile.write ( '\t@$(FC) -c $(SRC_DIR)/assert_class.f90\n' )
		self.makefile.write ( '\n' )
		self.makefile.write ( 'clean:\n' )
		self.makefile.write ( '\trm -f $(OBJ) $(MOD) TestRunner.f90 a.exe makeclean\n' )
		# self.makefile.write(text)



	# def compile_makefile(self):
		# self.target.write(_fun)
		# os.system('make')
		# os.system('make clean')



# arg1 = 'circle_class'
# arg2 = 'circle_class_test'
# c = Compiling(arg1, arg2)
# # c.write_to_makefile()
# c.compile_makefile()