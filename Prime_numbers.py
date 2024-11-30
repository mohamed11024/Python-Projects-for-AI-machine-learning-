for num in range(2,100):
    Prime = True
    for i in range(2,num):
        if num % i == 0:
            Prime = False
            break

    if Prime:
        print(num)            