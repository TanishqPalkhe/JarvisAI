lis=["Tanishq is very good","he is good is best","tanishq awsome tanishq "]
query=input("enter your query you wnt to search")
d=query.lower()
k=[]
if d not in str(lis):
    print("word is not available")
else:
    if d in str(lis):
        for i in range (len(lis)):
            a=lis[i].split(" ").count(d)
            k.append(a)
            print(k)
        ziper=zip(lis,k)
        ziper=list(ziper)
        res = sorted(ziper, key=lambda x: x[1],reverse=True)
        for ty in res:
            print(ty)










