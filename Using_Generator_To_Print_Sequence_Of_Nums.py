# 0 1 1 2 3 5 8 13 21 .........


def Fib():
    a , b = 0 , 1
    while True:
        yield a
        a , b = b , a+b

for i in Fib():
    if i > 21:
        break
    print(i)


