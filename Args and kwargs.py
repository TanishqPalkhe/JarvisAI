

name= "tanishq"
for alphabets in name:
    print(alphabets)
def funargs(normal1,args):
    print(normal1)
    for item in har:
        print(item)
har = ["carry", "marry", "harry"]
normal1 = "holly ye lo"
funargs(normal1,har)


def funargs(normal1, *har, **kw):
    print(normal1)
    for item in har:
        print(item)
    for key ,value in kw.items():
      print(key,value)


normal1="the list of students for programme"
var=["harry","rohan","hamid","yoo honey singh"]
fr=["dad",9,9,"tr"]
d2={"Rohan": "police", "Harry": "doctor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal1,*var,**d2)

import time
initial=time.time()
for i in range (0,5):
    time.sleep(1)
    print("hello")

def addition(a,b):
    return a+b+9

def printhar(string):
    return f"hello dude {string}"

if __name__ =='__main__':
    print(addition(2,8))
    print(printhar("tanishq"))
def positive_negative(a):
    if a>0:
        return "positive"
    elif a<0:
        return "negative"
print(positive_negative(-23))



numbers=[7,8,9]
numbers=list(map(lambda x:x*2,numbers))
print(numbers[2])
list1=[3,4,5,6,7,8,9]
def greater (num):
    return num>5
greater=list(filter(greater,list1))
print(greater)
from array import*
arr=array('i',[])
n=int(input("enter yr number"))
for i in range (n):
    q=int(input("value"))
    arr.append(q)
print(arr)
val=int(input("enter the value for search"))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
from numpy import*
arr=((5,6,9,0,8),(4,5,2,8,0,1))
print(arr)













