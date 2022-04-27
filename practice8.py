import random
def rohan(number):
    table = []
    for i in range(1,11):
        a=random.randint(0,9)
        b=random.randint(0,10)
        table.append(i*number)
    table[a]=table[a]+b
    return table

def iscorrect(table,number):
    for i in range(1,11):
        if table[i-1]!= i*number:
            return i-1
    return None
if __name__=='__main__':
    number=int(input("enter the number"))
    mytable=rohan(number)
    print(mytable)
    wr=iscorrect(mytable,number)
    print(f"incorrect position is {wr}")