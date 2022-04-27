
import time
from functools import lru_cache
n=int(input("enter the values you want to cache"))
@lru_cache(maxsize=n)
def add_two(x,y):
    time.sleep(n)
    return x+y
print(add_two(7,5))
print(add_two(9,8))
print(add_two(7,51))
print("hello")
print(add_two(7,5))

f1=open("tp.txt")
try:
    f=open("tu.txt")
except Exception as e:
    print(e)
else:
    print("great")
finally:
    print("run this anyway")
    f1.close()
print("cool")


def add(x,y):
    try:
        print(f"divided number{x//y}")
    except Exception as e:
        print(e)
    else:
        print("done")
add(8,0)
#corotines

def searcher():
    import time
    book="Tanishq is a good boy in the history of world"
    time.sleep(3)
    while True:
        text=(yield)
        if text in book:
            print("my name in book")
        else:
            print("my name not exist")
search=searcher()
print("welcome to corotines")
next(search)
search.send("Tanishq")
search.send("girl")
input()
print("hello cool")
search.send("boy")
f=open("tp.txt","w")

a=f.write("yoo honey")
b=f.write("hello")
