#Control statements

num = -1

if num > 0:
    print("this number is positive")
elif num == 0:
    print("this number is zero")       
else:
    print("this is negative")    
    
num1 = int(input("enter the first number: "))   
num2 = int(input("enter the second number: ")) 

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)   
else:
    print("both numbers are equal")     