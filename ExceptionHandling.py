num1 = input("Please Enter Num1: ")
num2 = input("Please Enter Num2: ")

try:
    z = (num1)/int(num2)

except ZeroDivisionError as e:
    print('Division by zero exception')
    z = None
except TypeError as e:
    print('Exception type error')
    z = None



print(z)