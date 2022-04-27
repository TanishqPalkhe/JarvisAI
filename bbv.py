from numpy import array

with open("poem.txt") as f:
    d = f.read().split("\n")
    for content in d:
        s = content.capitalize()
        with open("poem.txt", 'w') as f:
            f.write(s)


# import os
# p=r"C:\Users\hp\PycharmProjects\pythonProject\cool1\avengers.jpg"
# os.startfile(p)
def swap(l1):
    l1[0], l1[len(l1) - 1] = l1[len(l1) - 1], l1[0]
    print(l1)


list = [34, 67, 21, 45]
swap(list)


def student_data(*args):
    print(args[1])
    print(f"name of student is {args[0]} and class is {args[2]}")


student_data("tany", "se345", 5)
student_data("rtyty", "s90345", 10)


class student:
    def __init__(self, name, id, rollno):
        self.name = name
        self.id = id
        self.rollno = rollno


a = student("tanisgq", "r567", 89)
print(a.__dict__)


class student:
    pass


class marks:
    pass


raj = student()
uvi = student()
physics = marks()
maths = marks()
print(isinstance(raj, student))
print(isinstance(uvi, marks))
print(issubclass(marks, object))

for i in range(3):
    print("twinkle twinkle littile star")
    print("       ", end="")
    print("how i wonder what you are")
    print("                ", end="")
    print("Up above the world so high")
    print("                ", end="")
    print("like a diamond in the sky")
# filename=input("t")
# fg=filename.split(".")[1]
# print(fg)
p = (1, 3, 5)
j = str(p)
r = j.replace(",", "/")
print(r)
l1 = "tyui"
t = len(l1)
print(t)
z = [4, 67, 8, 8]
for i in range(4):
    a = z.count(z[i])
    print(a)

o = []
l = ["car", "loki", "kite", "dictionary", "shelter"]
for e in l:
    a = len(e)
    o.append(a)


def fan():
    for i in range(len(o)):
        if o[i] == max(o):
            return i


a = fan()
print(f"longest string is {l[a]}")
lis = [18, 19, 5, 5, 5, 3, 1]
d = lis.count(19)
k = lis.count(5)
if d == 2 and k >= 3:
    print("True")
else:
    print("false")
l = []
n = int(input("enter no of stones"))
for i in range(n):
    l.append(2 * i + n)
print(l)
k = []
d = [2, 4, 2, 3, 1, 1, 4, 2]
for i in range(4):
    if len(set(d)) < 4:
        print("false")
    else:
        print("true")
g = []
o = ["cars", "dog", "superman", '']
for e in o:
    r = len(e)
    g.append(r)
print(g)


def raj(strs, substr):
    p = []
    for s in strs:
        if substr in s:
            p.append(s)
    return p


strs = ['cat', 'car', 'fear', 'center']
print(raj(strs, "en"))
print(enumerate(strs))


# k=[s for s in strs if substr in s]
def fun(l):
    if " " in l:
        print(l.split(" "))
    elif "," in f:
        print(l.split(","))


fun("a b c d")
i = 1
a = [1, 2, 3, 4]
for r in a:
    if i % 2 != 0:
        print(r)
    i += 1

a = [6, 5, 4, 3, 3]
for i in range(len(a) - 1):
    pass
if a[i] < a[i + 1]:
    print('increasing')
elif a[i] > a[i + 1]:
    print('decreasing')
else:
    print("no monotonic")
j = []


def fan(a):
    for item in a:
        if " " in item:
            print("true")
        else:
            print("false")


a = ["car", "kite", "loly", "ce t"]
fan(a)
# u=input("enter no")

def divisor(n):
    l = []
    for i in range(1, 9000):
        if n % i == 0:
            l.append(i)
    l = l[:-1]
    print(max(l))
divisor(6500)
import math
def area():

    name=int(input("enter no of sides"))
    if name==3:
        a=int(input("enter a"))
        b=int(input("enter b"))
        c=int(input("enter c"))
        s=a+b+c/3
        print(math.sqrt(s*(s-a)* (s-b)*(s-c)))

    elif name==2:
        a = int(input("enter a"))
        b = int(input("enter b"))
        print(a*b)
    elif name==1:
        a=int(input("enter a"))
        print(a*a)
    else:
        print("invalid")
area()
shape=input("enter shape")
def volume(shape,*args):

    if shape=="cube":
        a = int(input("enter a"))
        print(a*a*a)
    elif shape=="cuboid":
            a = int(input("enter a"))
            b = int(input("enter b"))
            c = int(input("enter c"))
            print(a*b*c)
    elif shape=="cylinder":
        a = int(input("enter a"))
        b = int(input("enter b"))
        print(3.14*a**2*b)

volume(shape,2,3)
d={"name":"tanishq","age":19,"profession":"coder"}
d["profession"]="programmer"
print(d)

class student:
    def get(self):
        self.rollno=int(input("enter roll no"))
        self.mark1=int(input("enter marks 1"))
        self.mark2=int(input("enter marks 2"))

class sports():
    def getsm(self):
        self.sportsmarks=int(input("enter marks"))


class statement(student,sports):
    def totalmarks(self):
        return self.mark1+self.mark2+self.sportsmarks
    def average(self):
        return self.mark1+self.mark2+self.sportsmarks/3
    def getta(self):
        return f"student of {self.rollno} has marks in three subjects out of 100 are {self.mark1} {self.mark2} and  {self.sportsmarks}"
    def result(self):
        self.get()
        self.getsm()
        print(self.getta())
        print(self.totalmarks())
        print(self.average())

a=statement()
a.result()





























