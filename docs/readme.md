Funit: Fortran Unit Testing
===========================

## What is Funit? 

**funit** is a unit test tool for fortran language. It is based on python 2.7 and Gnu-make.

I develop the **funit** alone and for my own using, so it is incomplete, and have some drawbacks.



## To install

To install **funit**, simply clone this repository.

and run `bin/funit -h` in the shell, this will show the manual.

Optional, you could make a soft link of `bin/funit` under your `local/bin` directory.


## How to use it?

Suppose you have a Fortran Project:

+ Fortran
	+ src
	+ tests

+ Fortran/src
	- circle_class.f90

+ Fortran/tests
	- circle_class.test

`circle_class.f90` is a fortran program which contains a single module. Put it under `src/` directory.

To test `circle_class.f90`, you need a test program class_A.test. Put your `.test` file under `tests/` directory.


``` bash 
$ cd funit
$ bin/funit -t circle_class.test 
```
It will test circle_class.f90 

or simply 
``` bash
$ bin/funit
```
It will test all `.test` files in `test/` directory

Results will be print on the shell sreen.

After that, you could remove the temporary file by command
``` bash
$ make clean
```

You can find both `circle_class.f90` and `circle_class.test` are in the Funit repository.

## things have to mention

1. The fortran source files which need to be test shall be put into $(PROJECT)/src/ , and test files should be put into $(PROJECT)/tests/. The source and test files share same names. 


2. The grammer to write `.test` file is same as write a fortran module

``` fortran
module test_circle
	use circle_class
	use assert_class ! shall be included in every .test file
	implicit none
contains
	subroutine setup
	! code here run before each test
	end subroutine

	subroutine teardown
	! code here run after each test
	end subroutine

	subroutine test_assert
		call assert_equal(1,1)
		call assert_real_equal(1.e0,1.e0)
	end subroutine
end module
```
## To do

A script to setup fortran project automatically.