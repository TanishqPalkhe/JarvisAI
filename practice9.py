import random
n=int(input("enter the no of friends"))
l=[]
o=[]
p=[]
for i in range (n):
    user=input(f"enter the name of friend{i+1}")
    l.append(user)
for ty in l:
    r=ty.split(" ")
    o.append(r[1])
    p.append(r[0])
for i in p:
    print(i+" "+ random.choice(o))


























