class op:
    no_leaves="here in op"
    def __init__(self):
        self.name="i am in op"
        self.no_leaves="var in op"
        self.hobby="i am cool"


class abc(op):
    no_laeves="here in abc"
    def __init__(self):

        self.name="i am in abc"
        self.no_leaves="var in abc"
        super().__init__()
Alex=op()
Aj=abc()
print(Aj.no_leaves)
print(Aj.hobby)
from abc import ABC ,abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    def __init__(self):
        self.length=4
        self.breath=5
    def printarea(self):
         return self.length*self.breath
AS=rectangle()
print(AS.printarea())
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{self.fname},{self.lname}rtuy2544@.com"
    @property
    def email(self):
        if self.fname==None and self.lname==None:
            return "email not found"
        return f"{self.fname},{self.lname} tuiy5667@.com"

    @email.setter
    def email(self,string):
        print("hello")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

Tanishq=Employee("tanishq","palkhe")
kunal=Employee("kunal","sharma")
Tanishq.fname="tanay"
print(Tanishq.email)
Tanishq.email="tanny.this@557.com"
print(Tanishq.fname)
print(Tanishq.email)
del Tanishq.email
print(Tanishq.email)

#online library

class library:
    def __init__(self,list_of_books,library_name,dictonary):
        self.list_of_books=list_of_books
        self.library_name="Tanishq Library"
        self.dictonary={}


    def display(self):
        return f"our library is {self.list_of_books}"

    def lend(self):
        book=input("select the book you want to take")
        name=input("enter your name")
        if book in self.list_of_books:
            self.dictonary[book] = name
            self.dictonary.update({book:name})
            self.list_of_books.remove(book)
            print(Tanishq.list_of_books)
            print("ok you can take")
        else:
            print(f"this book is not available it is taken by  {self.dictonary[book]}")


    def add(self):
        ask=input("which book you want to add")
        self.list_of_books.append(ask)
        print(Tanishq.list_of_books)
        return "book added successfully"

    def retur(self):
        say=input("enter the name of book you want to return")
        if say  in self.list_of_books:
            print("you have not lend this book")
        else:
            self.list_of_books.append(say)
            print("your book has been returned")
            print(self.list_of_books)



Tanishq=library(["spiderman2","aladin","the taj","aquaman","pop prince","antman"],"tanishq library",{})
print(f"WELCOME to {Tanishq.library_name}")
while True:
        user_input = int(input("enter 1 for display 2 for lend 3 for add and 4 for retur"))
        if user_input==1:
            print(Tanishq.display())
        elif user_input==2:
            print(Tanishq.lend())
        elif user_input==3:
            print(Tanishq.add())
        elif user_input==4:
            print(Tanishq.retur())

        else:
            print("invalid")



