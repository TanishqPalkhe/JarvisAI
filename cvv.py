X=[[2,4,3],
   [6,8,9],
   [5,1,2]]
def sum(X):
    p=0
    o=0
    u=0
    for i in range(len(X[0])):
        p=p+X[i][0]
        o=o+X[i][1]
        u=u+X[i][2]
    print("sum of first row is",p)
    print(f"sum of second row is",o)
    print(f"sum of third row is",u)
sum(X)
def sqarea(n):
    return n*n
def rectarea(n1,n2):
    return n1*n2
def ciarea(r):
    return 3.14*r**2
def triarea(a,b,c):
    s=(a+b+c)/2
    area=(s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
# user=int(input("enter 1 for square, 2 for rectangle, 3 for circle and 4 for triangle"))
# if user==1:
#     n=int(input("enter a side of square"))
#     print("area of square is",sqarea(n))
# elif user==2:
#     n1 = int(input("enter a side of rectangle"))
#     n2 = int(input("enter another side of rectangle"))
#     print("area of rectangle is", rectarea(n1,n2))
# elif user==3:
#     r = int(input("enter radius of circle"))
#     print("area of circle is", ciarea(r))
# elif user==4:
#     a=int(input("enter a"))
#     b=int(input("enter b"))
#     c=int(input("enter c"))
#     print("area of triangle is", triarea(a,b,c))
def facto(n):
    p=1
    for i in range(0,n):
        p=p*(i+1)
    return p
n=int(input("enter the value of n"))
p=0
for i in range(1,n+1):
    p1=p+i/facto(i)
    p2 = -p1
    p = p2
    print(p)






