FC = gfortran
FLAGS = -g

PRO_DIR = /Users/shiqi/Projects/funit
SRC_DIR = $(PRO_DIR)/src
TEST_DIR = $(PRO_DIR)/tests

OBJ = *.o
MOD = *.mod

a.exe: TestRunner.f90 test.o
	$(FC) $(FLAGS) $(OBJ) TestRunner.f90 -o a.exe

test.o: $(TEST_DIR)/circle_class_test.f90 src.o assert_class.o
	$(FC) -c $(TEST_DIR)/circle_class_test.f90

src.o: $(SRC_DIR)/circle_class.f90
	$(FC) -c $(SRC_DIR)/circle_class.f90

assert_class.o: $(SRC_DIR)/assert_class.f90
	$(FC) -c $(SRC_DIR)/assert_class.f90

clean:
	rm -f $(OBJ) $(MOD)
