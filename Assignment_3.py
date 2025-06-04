
#Task 1: Calculate Factorial Using a Function 
x=int(input("Enter a number :"))
def factrl(a):
    if a==0 or a==1:
        return 1
    else:
        b=a*factrl(a-1)   #here the factorial works recursively
        return b
result=factrl(x)
print (f"Factorial of {x} is : {result}")

#Task 2: Using the Math Module for Calculations

from math import *
a=int(input("Enter a number: "))

print(f"Square root : {sqrt(a)}")
print(f"Logatithm : {log(a)}")
print(f"Sine : {sin(a)}")
