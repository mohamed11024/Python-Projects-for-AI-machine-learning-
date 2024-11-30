import numpy as np
import sys as s
import time as t

SIZE  = 1000000
list1 = range(SIZE)
list2 = range(SIZE)

array1 = np.arange(SIZE)
array2 = np.arange(SIZE)

start1 = t.time()

res1 = [(i+j) for i,j in zip(list1,list2)]
print("time for lists are ",(t.time() - start1)*1000)

start2 = t.time()
res2 = array1+array2
print("time for arrays are ",(t.time() - start2)*1000)


