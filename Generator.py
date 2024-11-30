def Remote_Control_Next():
    yield "Mo"
    yield "Ahmed"
    

itr = Remote_Control_Next()
print(itr)

#First way to do generator
print(next(itr))


#Second way to do generator
for i in Remote_Control_Next():
    print(i)


