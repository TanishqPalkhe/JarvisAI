a=10
X=[[2,5,7],
   [4,0,6],
   [5,2,1]]
Y=[[3,7,0],
   [8,0,1],
   [7,3,0]]
raw=[[0,0,0],
     [0,0,0],
     [0,0,0]]
def sum(X,Y):
    row=[]
    for i in range (0,3):
       o=[]
       for j in range (0,3):
          o.append(X[i][j]+Y[i][j])
       row.append(o)
    return row
print(sum(X,Y))
total=0
def sum(X,Y):
    row=[]
    for i in range (0,1):
       o=[]
       for j in range (0,3):
          o.append(X[0][j]+X[0][j]+X[0][j])
       row.append(o)
    return row
print(sum(X,Y))

print(X[0][0]+X[0][1]+X[0][2])
for i in range (0,3):
    for j in range (0,3):
            raw[j][i]=X[i][j]
for r in raw:
    print(r)
i=0
while i<5:
    print(i)
    i+=1
# def tables():
#     for i in range(2,11):
#         print("")
#         for j in range(1,11):
#             print(i*j,end=" ")
# tables()
# n1=int(input("enter first number"))
# n2=int(input("enter first number"))
# n3=int(input("enter first number"))
# # def func():
# #     if n1>=n2 and n1>=n3:
# #         print(f"{n1} is largest")
# #     elif n2>=n1 and n2>=n3:
# #         print(f"{n2} is largest")
# #     else:
# #         print(f"{n3} is largest")
# # func()
l=[2,4,5,8,78,77]
def even():
    print("even numbers from list are")
    for i in range(len(l)):
        if l[i]%2==0:
            print(l[i])


even()
s="tanishq"
def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str
print(reverse(s))
k=[]
for i in range(2,50):
    s=i**2
    k.append(s)
print(k)
n=int(input("enter number"))
k=str(n)
if k==k[::-1]:
    print("it is palendrome")
else:
    print("nor")


l=[1,2,2,4,5,6,7,8.6]
def unique():
    mylist=set(l)
    newlist=list(mylist)
    return newlist
print(unique())

class student:
    def studentinfo(self):
        self.name=input("enter name")
        self.rollno=int(input("enter roll no"))
    def marks(self):
        self.p=int(input("enter the marks of physics"))
        self.c=int(input("enter the marks of chemistry"))
        self.b=int(input("enter the marks of biology"))
        self.m=int(input("enter the marks of maths"))
        self.s=int(input("enter the marks of social"))


class result(student):
    def student(self):
        return f"name of student is {self.name} and roll no is{self.rollno}"
    def percentage(self):
        return "total percentage", (self.p + self.c + self.b + self.m + self.s) / 500 * 100
    def showresult(self):
        self.studentinfo()
        self.marks()
        print(self.student())
        print(self.percentage())

a=result()
a.showresult()










