
f = open("C:\\Read_Write_Files\\file1.txt","r")
W = open("C:\\Read_Write_Files\\file2.txt","w")

for line in f:
    tokens = line.split(' ')
    W.write(line + " Word Count: " + str(len(tokens)))
    

f.close()
W.close()