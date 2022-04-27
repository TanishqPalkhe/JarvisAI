list = []
orglist=[]
n=int(input("enter the no of items"))
for i in range(n):
    list.append(int(input("enter the list element\n")))
    orglist =list.copy()
print(list)

reverse3=list[:]
for j in range (0,len(list)):
    list[j]=orglist[n-1-j]
print(list)
reverse1=list[:]
reverse1.reverse()
print(list)
reverse2=list[::-1]
print(list)
if reverse1==reverse2==reverse3:
    print("yes ")
    #or another method for swaping
#for i in range(len(a)//2):
	#a[i],a[-(i+1)] = a[-(i+1)], a[i]




    










