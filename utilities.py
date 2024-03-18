import sys 
import ctypes

def size_of_attribute(struct, attribute):
    return ctypes.sizeof(getattr(struct(), attribute))