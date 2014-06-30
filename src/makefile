
FC = gfortran
FLAGS = -g -WALL

OBJ = *.o
MOD = *.mod

a.exe: main.f90 $(OBJ)
	$(FC) $(FLAGS) $(OBJ) main.f90 -o a.exe

test_class.o: test_class.f90
	$(FC) -c test_class.f90

assert_class.o: assert_class.f90
	$(FC) -c assert_class.f90

clean:
	rm -f $(OBJ) $(MOD)
	