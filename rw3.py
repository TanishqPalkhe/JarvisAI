with open("cv.txt") as f:
    file1=f.read().split("\n")
    for content in file1:
        dad=content.capitalize()
        print(dad)
def file(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file  {filename} not found")
file("tut1.txt")
file("tut5.txt")
file("tut3.txt")

l1=[1,2,3,4,5,6,7,8,9]
for i,items in enumerate(l1):
    if i ==2 or i==4 or i==6:
        print(f"{items} are{i+1}")
n=int(input("enter"))
l=[n*i for i in range(1,11)]
#print(l)
with open("tut1.txt",'a') as f:
    f.write(str(l))
    f.write("\n")

a=int(input("e"))
b=int(input("e"))
if b==0:
    raise ZeroDivisionError("infinte")
else:
    print(a/b)
name=(input("enter name"))
marks=int(input("enter marks"))
phone=int(input("enter no."))
def format(name,marks,phone):
    return f"Name of the student is {name},his marks are {marks} and phone number is {phone}"
a=format(name,marks,phone)
print(a)
l=[2,5,10,6,20,7,35]

o=list(filter(lambda x:x%5==0,l))
print(o)
from functools import reduce
l5=[1,5,3,9,7,5]
a=reduce(max,l5)
print(a)