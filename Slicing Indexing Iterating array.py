import numpy as np


a = np.array([1,2,3])
print(a[0:2])

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[1,1])

for row in b:
    print(row)




for row in b:
    for col in row:
        print(col)


for i in b.flat:
    print(i)

c = np.arange(9).reshape(3,3)    
print(c)

d = np.vstack((b,c))
print(d)

e = np.hstack((b,c))
print(e)


f = np.arange(30).reshape(2,15)
g = np.hsplit(f,3)
print(g)
h = np.vsplit(f,2)
print(h)

I = np.arange(12).reshape(3,4)
J = I > 3
print(J)

print(I[J])

I[J] = 1
print(I)
