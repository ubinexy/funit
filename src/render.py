# -*- coding: utf-8 -*-  

# import 

def header():
    header = '''
program main
    use a_class
    implicit none
    real(8) :: a
    real(8) :: b
    '''
    print header

def footer():
    footer = '''
end program
    '''
    print footer

####################

def tear():
    print 'tear file'



def render():
    setup_doc ='''
    ! Place code here that should run before each test
    '''

    teardown_doc = '''
    ! This code runs immediately after each test
    '''

    assert_doc ='''
    assert_equal(1, 5, 4)
    '''


    print setup_doc
    print assert_doc
    print teardown_doc

# 

header()
render()
footer()