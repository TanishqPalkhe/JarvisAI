number=input("entr any number")
total=0
for i in range (0,len(number)):
    total=total+int(number[i])
print(total)


p=int(input("enter a number"))
r=int(input("enter a number"))
t=int(input("enter a number"))
s=p*r*t/100
print(s)
n=int(input("enter"))
c=((n-32)*5)/9
print(f"temperature in celcius{c}")
m=int(input("enter columns"))
n=int(input("enter rows"))
def matrics(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range (n):
            inp=input(f"p{i}{j}")
            row.append(inp)
        o.append(row)
    return o
A=matrics(m,n)
print(A)

B=matrics(m,n)
print(B)
def sum(A,B):
    output=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output
s=sum(A,B)
print(s)



