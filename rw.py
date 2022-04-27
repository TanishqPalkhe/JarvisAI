import os
def facto(n):
    if n==1 or n==0:
        return 1
    else:
        return n*facto(n-1)
print(facto(4))
def sum(n):
    if n==0:
        return 0
    else:
        return (n%10)+(sum(int(n/10)))
print(sum(5))
l=["is","yo" ,"areso" ,"cool","red" ,"in" ,"sky"]
def func(word):
    l.remove(word)
    l.append(word)
    return l
print(func("cool"))
def multi(n):
    for i in range (1,11):
        s=n*i
        print(s)
print(multi(8))
n=int(input("ee"))
with open("poem.txt") as f:
    d=f.read()
    if "cool" in d:
        print("yes")
    else:
        print("no")
#os.makedirs("cool")
        for j in range(2, 21):
            with open(f"cool/doo{j}", 'w') as f:
                for i in range(1,11):
                    a=f.write(f"{j}X{i}={j*i}\n")
                if i!=10:
                    f.write('\n')
content=True
i=1
with open("hiscore1.txt") as f:
    while content:
        content=f.readline()
        if "python" in content:
            print(content)
            print(i)
        i+=1





