import numpy as np
import sys as s
import time as t

l  = range(1000)

array = np.arange(1000)

print(s.getsizeof(5)*len(l))
print(array.size * array.itemsize)


