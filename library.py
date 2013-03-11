#This Vishal file is used to call a C function from Python
#Change made in version branch
from ctypes import *
lib = CDLL('./libvishal.so')
lib.show()
