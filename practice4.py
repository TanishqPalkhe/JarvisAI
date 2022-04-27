n=int(input("enter no of string"))
l1=[]
for i in range(n):
    user=int(input("enter no "))
    l1.append(user)
#print(l1)
for j in l1:
    while True:
        k=str(j)
        if k[:]==k[::-1]:
            print(f"next pelendrome is {int(k)}")
            break
        else:
            j=j+1






    



















