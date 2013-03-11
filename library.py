#This file is used to call a C function from Python
from ctypes import *
lib = CDLL('./libvishal.so')
lib.show()
