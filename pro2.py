f = open("C:\\Read_Write_Files\\fil3.txt","r")


i=0
def countNum(Num):
    count = 0
    for line in f:
        tokens = line.split(',')
        for i in tokens[0],tokens[1]:
                if(Num == int(i)):
                     count+=1
    return count


for line in f:
    tokens = line.split(',')
    sum = 0
    for i in tokens:
        sum += int(i)
    f.write("summation: " + str(sum) + " | ")

f.close()
        


#res = countNum(0)
