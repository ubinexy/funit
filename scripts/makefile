FC = gfortran
FLAGS = -g 

PRO_DIR = /Users/shiqi/Projects/funit
SRC_DIR = $(PRO_DIR)/src
TESTS_DIR = $(PRO_DIR)/tests

OBJ = *.o
MOD = *.mod

a.exe: TestRunner.f90 circle_class.o assert_class.o
	$(FC) $(FLAGS) $(OBJ) TestRunner.f90 -o a.exe

circle_class.o: $(SRC_DIR)/circle_class.f90
	$(FC) -c $(SRC_DIR)/circle_class.f90

assert_class.o: $(SRC_DIR)/assert_class.f90
	$(FC) -c $(SRC_DIR)/assert_class.f90

clean:
	rm -f $(OBJ) $(MOD)
