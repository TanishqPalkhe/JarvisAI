X=[[1,3,2],
   [3,8,9],
   [2,4,7,]]
Y=[[7,0,4],
   [5,2,1,],
   [5,7,9]]
from array import*
arr=array('i',[])

for i in range (len(X)):
   for j in range (len(Y)):
       arr.append(X[i][j]+Y[i][j])
   print(arr)


   #Health Management
def get_Date():
    import datetime
    return datetime.datetime.now()

user_input=int(input("press 1 for log and 2 for retrieve"))
if user_input==1:
       p = int(input("press 1 for harry 2 for rohan 3 for habib"))
       if p==1:
           l = int(input("enter 1 for exercise and 2 for diet"))
           if l==1:
               n=input("enter your exercise")
               with open ("harry exercise","a") as f:
                 f.write(n + str(get_Date()))
                 f.close()
                 print("enter successfully")
           elif l==2:
               n = input("enter your diet")
               with open("harry diet","a") as f:
                 f.write(n+str(get_Date()))
                 f.close()
       elif p==2:
           l = int(input("enter 1 for exercise and 2 for diet"))
           if l == 1:
               n = input("enter your exercise")
               with open("rohan exercise","a") as f:
                 f.write(n+str(get_Date()))
                 f.close()
                 print("enter successfully")
           elif l == 2:
               n = input("enter your diet")
               with open("rohan diet","a") as f:
                 f.write(n+str(get_Date()))
                 f.close()
       elif p==3:
           l = int(input("enter 1 for exercise and 2 for diet"))
           if l == 1:
              n = input("enter your exercise")
              with open("habib exercise","a") as f:
                f.write(n+str(get_Date()))
                f.close()
                print("enter successfully")
           elif l == 2:
              n = input("enter your diet")
              with open("habib diet","a") as f:
                f.write(n+str(get_Date()))
                f.close()


elif user_input==2:
       p=int(input("press 1 for harry 2 for rohan 3 for habib"))
       if p== 1:
          l = int(input("enter 1 for exercise and 2 for diet"))
          if l == 1:
              with open("harry exercise","rt") as f:

                print(f.read())
                f.close()

          elif l == 2:
              with open("harry diet","rt") as f:
                conten=f.read()
                print(conten)
                f.close()

       elif p == 2:
          l = int(input("enter 1 for exercise and 2 for diet"))
          if l== 1:
              with open("rohan exercise","rt") as f:
                cntent=f.read()
                print(cntent)
                f.close()

          elif l== 2:
              with open("rohan diet","rt") as f:
                kilo=f.read()
                print(kilo)
                f.close()

       elif p== 3:
          l = int(input("enter 1 for exercise and 2 for diet"))
          if l == 1:
              with open("habib exercise","rt") as f:
                 oye=f.read()
                 print(oye)
                 f.close()

          elif l == 2:
               with open("habib diet","rt") as f:
                 kvs=f.read()
                 print(kvs)
                 f.close()
else:
    print("invalid")









