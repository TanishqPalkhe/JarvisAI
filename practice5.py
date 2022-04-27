n=int(input("enter how many no. you want to print"))
list=[]
o=[]
for i in range (n):
    user=int(input("enter numbers"))
    list.append(user)
print(list)
for er in list:
    while True:
        k=str(er)
        if k[:]==k[::-1]:
            o.append(er)
            break
        else:
            er+=1
print(o)



