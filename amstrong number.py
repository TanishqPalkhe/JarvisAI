n=int(input("enter number"))
s=0
for i in range(0,len(str(n))):
    p=str(n)
    u=p[i]
    k=int(u)
    p=k**len(str(n))
    s=s+p
print(s)
if s==n:
    print("its an amstrong number")
else:
    print("not an amstrong number")
