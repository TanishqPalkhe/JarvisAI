class calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        return self.num*self.num

    def cube(self):
        return self.num**3

    def square_root(self):
        return self.num**1/2
    @staticmethod
    def greet():
        print("hello friends")

number=calculator(4)
number.greet()
print(number.square_root())

class train:
    def __init__(self,book_ticket,status,fair):
        self.book_ticket=book_ticket
        self.status=status
        self.fair=fair
    def icket(self):
        return f"your ticked has been booked to {self.book_ticket}"
    def op(self):
        return f"no of seats left {self.status}"
    def dp(self):
        return f"total fair cost {self.fair}"
    def book(self):
        if self.status>0:
            print(f"your seat number is {self.status}")
            self.status=self.status-1
        else:
            print("seat not available")

stabdi=train("stabdi express",56,890)
print(stabdi.dp())
print(stabdi.book())
print(stabdi.book())
print(stabdi.icket())
class employee:
    da=9
    def __init__(self,name,name1):
        self.name=name
        self.name1=name1
    @classmethod
    def df(cls,new):
        cls.da=new

    @property
    def email(self):
        return f"your email is {self.name}{self.name1}34@gamil.com"
tanishq=employee("tanishq","palkhe")

print(tanishq.email)
tanishq.df(34)
print(tanishq.da)
class vector1:
    def __init__(self,i,j):
        self.i=i
        self.j=j

class vector2(vector1):
    def draw(self,i,j,k):
        super().__init__(i,j)
        self.k=k
        return f"your vector is {self.i}i+{self.j}j+{self.k}k"
s=vector2(3,6)
print(s.draw(3,7,6))

class employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    @property
    def salaryafterincrement(self):
        return self.salary*self.increment
    @salaryafterincrement.setter
    def salaryafterincrement(self,new):
         self.increment=new/self.salary


e=employee(20000,1.5)
e.salaryafterincrement=50000
print(e.increment)

print(e.salaryafterincrement)

class complex:
    def __init__(self,a,b):
        self.real=a
        self.imaginary=b
    def complexnumber(self):
        return f"complex number is {self.real}+{self.imaginary}i"
    def __add__(self,other):
        return complex(self.real+other.real,self.imaginary+other.imaginary)
    def __str__(self):
        return f"complex number  {self.real}+{self.imaginary}i"

a=complex(3,5)
b=complex(8,7)
print(b.complexnumber())
print(a+b)

class vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str=""
        index=0
        for i in self.vec:
            str+=f"{i}a{index}+"
            index+=1
        return str[:-1]
    def __mul__(self,other):
        l=[]
        for i in range(len(self.vec)):
                l.append(self.vec[i]*other.vec[i])#dot product of vector
        return vector(l)

    def __len__(self):
        return len(self.vec)

c=vector([7,5,4])
u=vector([2,6,8])
print(c*u)
print(len(c))

class student:
    def studentinfo(self):
        self.name=input("enter name of student")
        self.roll=int(input("enter roll no for student"))
    def displayroll(self):
        return f"Name of student is {self.name} and roll no. is {self.roll}"
class subject(student):
    def getmarks(self):
        self.p=int(input("p"))
        self.c=int(input("c"))
        self.m=int(input("m"))
    def display_marks(self):
        return f"marks in different subjects are {self.p},{self.c},{self.m}"
    def total(self):
        return self.p+self.c+self.m
class result(subject):
    def result(self):
        self.studentinfo()
        self.getmarks()
        print(self.displayroll())
        print(self.display_marks())
        print(f"total marks obtained from 300 are{self.total()}")
s=result()
s.result()


class person:
    count_instance=0
    def __init__(self,name):
        person.count_instance += 1
        self.name=name

p1=person("tanishq")
p2=person("tanishq")
p3=person("tanishq")
p4=person("tanishq")
print(person.count_instance)










