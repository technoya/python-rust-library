import ctypes
import time
# Load the Rust shared library
lib = ctypes.CDLL("module/count_timer_lib.dll")  # Adjust path and library name as necessary

# Define function prototype
lib.count_up_to.argtypes = [ctypes.c_ulonglong]
lib.count_up_to.restype = ctypes.c_ulonglong

def num(num):
 v1=lib.count_up_to(num)
 return v1