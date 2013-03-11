from ctypes import *
lib = CDLL('./libvishal.so')
lib.show()
