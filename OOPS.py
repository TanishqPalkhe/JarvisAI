def func1(dec1):
        print("do you know")
        dec1()
        def newaapa():
           print("in the world")
        return newaapa()
@func1
def name():
    print("tanishq is a good boy")

    #oop
class Employee:
    _no_leaves = 8
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary} and role is {self.role}"
    def __init__(self,name,salary,role):
        self.name=name
        self.role=role
        self.salary=salary
        #dunder method
    def __add__(self,other):
        return self.salary+other.salary
    def __str__(self):
        return f" is {self.name} salary is {self.salary} and role is {self.role}"

    def __repr__(self):
        return f"yo yo"



    @classmethod
    def change_leaves(cls,newleaves):
       cls.no_leaves=newleaves

    #@classmethod
    #def total(cls,string):
        #quto=string.split(",")
        #return cls(quto[0],quto[1],quto[2])
    @classmethod
    def total(cls,string):
       return cls(*string.split(","))

#1. "self" could be any object
#2. "def __init__(self)" allows to create or construct the instance variables whenever arguments are passed to the class or whenever an object is created.
#3. Class does not receive any arguments without a constructor


Kunal = Employee("Kunal", 34000, "instructor")
Tanishq=Employee("Tanishq",45000000,"Educator")
Aman = Employee.total("aman,45789,student")
Kunal.change_leaves(45)
print(Employee.no_leaves)
print(Aman.role)
print(repr(Tanishq))

Employee.no_leaves=12

print(Kunal.__dict__)
print(Kunal.salary,Kunal.no_leaves)
print(Kunal.printdetails())

#i=0
#while i<3:
    #user_input = input("enter your figure ")
    #if user_input=="rectangle":
     #  print("enter the sides of rectangle")
      # l1=int(input())
       #l2 = int(input())
       #i+=1
       #print(l1*l2)

    #elif user_input=="circle":
       #print("enter the radius of circle")
       #l1 = int(input())
       #print(3.14*l1**2)
       #i+=1

    #elif user_input=="triangle":
        #print("enter the sides of triangle")
        #l1 = int(input("enter base"))
        #l2 = int(input("enter height"))
        #print(0.5*l1*l2)
        #i+=1
class Programmer(Employee):
    def __init__(self,name,salary,role,language):
        self.name = name
        self.role = role
        self.salary = salary
        self.language=language

    def printdetails(self):
        return f"Programmer name is {self.name} salary is {self.salary} and role is {self.role} and language is{self.language}"

subham = Programmer("subham", 34000, "instructor",["cpp"])
Rahul = Programmer("Rahul", 45000000, "Educator",["cpp"])
print(Tanishq.printdetails())
print(subham.language)
class Player:
    no_leaves=9
    def __init__(self,name,game,age):
        self.name=name
        self.game=game
        self.age=age

    def printdetails(self):
        return f"Name of player is {self.name},he plays {self.game},and his age is {self.age}"

class coolprogrammer(Employee,Player):

    language="python"
    def py(self):
        print(self.language)

Arjun=Player("Arjun","cricket",23)
Karan=coolprogrammer("Karan","hockey",45)
print(Karan.printdetails())
print(Karan.py())
print(Karan.no_leaves)

class electronicgadgets:
    dad=9
    pass

class pocketgadgets(electronicgadgets):
    dad=8
    def __init__(self,name,gadget):
        self.name=name
        self.gadget=gadget
        self.special="this is cool"


class phone(pocketgadgets):
    def tota(self):
        return f"{self.name} has {self.gadget}"

Nitin=phone("nitin","ipod")
print(Nitin.special)
fazan=electronicgadgets()
print(fazan.dad)
print(Nitin.dad)
print(Nitin.tota())







def factorial(n):
    p = 1
    for i in range(n):
        p = p * (i + 1)
    return p
n=int(input("enter"))
total=0
for i in range (0,n):
    total=total+1/factorial(i)
    i+=1

print(total)

total=0
for i in range(0,4):
    total=total+i
    i+=1
print(total)













