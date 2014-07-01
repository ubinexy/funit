# -*- coding: utf-8 -*-  
import os
from compile import *
from render import *

dir = 

for f in os.listdir(dir)
	name, ext = os.path.splitext(f)

	if ext == 'fun':
		C = render(name)
		C = compile(name)
		execute(name)
	else:
		pass

def execute(name):

	if os.path.exists(a.InputFile):
		cmd = "cat a.InputFile | ./a.exe > a.OutputFile"
	else:
		cmd = "./a.exe > a.OutputFile"
	os.system(cmd)