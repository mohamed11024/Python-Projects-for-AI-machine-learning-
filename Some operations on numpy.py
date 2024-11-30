import numpy as np
import sys as s
import time as t


a = np.array([[1,2],[3,4],[5,6]])

print(a.itemsize)
print(a.ndim)
print(a.dtype)

b = np.array([[1,2],[3,4],[5,6]],dtype=np.float64)
print(b)

print(a.size)

print(a.shape)

c = np.array([[1,2],[3,4],[5,6]],dtype=np.complex_)
print(c)

d = np.zeros((3,2))
print(d)