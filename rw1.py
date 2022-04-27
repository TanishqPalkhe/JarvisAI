import random

a = 34


def factorial(n):
    s = 1
    for i in range(n):
        s = s * (i + 1)
    return s


def series(n):
    # a = 0
    for i in range(n):
        a = 1 / factorial(i + 1)
    return a


print(series(4))


def ser(n):
    s = 0
    sa = 0
    for i in range(n):
        s = s * 10 + 1
        sa += s
    return sa


print(ser(3))


def sm_div(func):
    def inner(a, b):
        if b > a:
            a, b = b, a
        return func(a, b)

    return inner


# print(sm_div(8,7))
@sm_div
def div(a, b):
    print(a / b)


div(3, 6)
y = "tanishq is a very good k"
f = y.replace("is", "was")
print(f)
print(y[1])

p = [2, 4, 5, 6]
p.remove(2)
print(p)

t = "tanishq  is  good k"

t = t.replace("  ", " ")
print(t)
letter = "Dear Harry, This Python course in nice. Thanks!!"
p = (7, 0, 8, 0, 0, 9)
s = p.count(0)
print(s)
# a=int(input("enter"))
# b=int(input("enter"))
# c=int(input("enter"))
# e=int(input("enter"))
# if a>b and a>c and a>e:
#   print("a is greater")
# elif b>a and b>c and b>e:
#  print("b is greater")
# elif c>a and c>b and c>e:
#   print("c is greater")
# else:
#   print("e is greater")
# eng=int(input("enter"))
# sst=int(input("enter"))
# math=int(input("enter"))
# if (eng+sst+math)/3<40 or eng<=33 or sst<=33 or math<=33:
#   print("fail")
# else:
#   print("pass")
# user=input("enter")
# if len(user)<10:
#   print("less than 10")
# else:
# print("greater than 10")
l="this is cool harry\"tanishq is great\"to yo"
if "harry" in l:
    print("yes")
else:
    print("no")
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
for item in l1:
    if item.startswith("S"):
        print("hello",item)


n=int(input("eeeee"))
if n>1:
    for i in range(2,n):
        if (n % i)==0:
            print("it is not prime")
            break
    else:
        print("it is prime")


l=[]
n=int(input("enter a number"))
for i in range(1,11):
    s=n*(i)
    l.append(s)
    l.sort(reverse=True)
for u in l:
    print(u)
n=int(input("eeeee"))
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))

n=int(input("eeeee"))
for i in range(n):
    print(" "*(n+1-2*i),end="")
    print("*"*(2*i+1))
n=int(input("eeeee"))

print("*"*n)
print("*"*1,end="")
print(" "*1,end="")
print("*"*1)
print("*"*n)




