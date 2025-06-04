# Task 1: Check if a Number is Even or Odd

a=int(input("Enter a number : "))

if a%2==0:  #the modulo operator (%) is used to find the remainder when one number is divided by another
    print(f"{a} is a Even number")
else:
    print(f"{a} is a odd number")

#Task 2: Sum of Integers from 1 to 50 Using a Loop
c=1
d=51
a=0
for i in range (c,d):
    #print(i)
    a=a+i
print(f"The Sum of numbers from {c} to {d-1} is : {a}")
