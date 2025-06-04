
#Task 1: Read a File and Handle Errors 
try:
    content=[]
    f_name="sample.txt"
    path=r"D:\sample.txt"
    with open (path,'r') as read_f:
        content=read_f.readlines()  # this function used to read line by line
except FileNotFoundError:
    print(f"Error : The file {f_name} was not found") 
finally:
    if content:
        for i,data in enumerate(content,start=1):
            print(f"Line {i} : {data.strip()}")

#Task 2: Write and Append Data to a File
a=input("Enter text to write to the file : ") #"I am additionally wrting this content in r+ mode to append to the existing sample'txt file"
try:
    #c_apnd=[]
    f_name="sample.txt"
    path=r"D:\sample.txt"
    with open (path,'a') as wrt_a:
        c_apnd=wrt_a.write("\n" + a)  # this function used to read line by line
except FileNotFoundError:
    print(f"Error : The file {f_name} was not found") 
finally:
    with open (path,'r+') as read_a:
        c_read=read_a.readlines()
        print(c_read)