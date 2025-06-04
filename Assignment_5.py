#Task 1: Create a Dictionary of Student Marks
std_marks={"Naveen":100,"Vidhya":99,"Vamikha":99,"Vishnu":100}

a=input("Enter the student's name: ")

if a in std_marks:
    print(f"{a}'s marks: {std_marks[a]}")
else:
    print("Student not found")

#Task 2: Demonstrate List Slicing 
lst=[1,2,3,4,5,6,7,8,9,10]
print(f"Original list {lst[:]}")
print(f"Extracted first five elements {lst[0:5]}")
print(f"Reversed Extracted elements {list(reversed(lst[0:5]))}")
print(f"Reversed Extracted elements {lst[0:5] [::-1]}")