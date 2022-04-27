a=int(input("number1"))
b=int(input("number2"))
if b==0:
    raise ZeroDivisionError("invalid")
else:
    print(f"your anser is{a/b}")
c=input("name")
if c=="harry":
    raise ValueError("harry is blocked")
else:
    print("hello")
x="av"
y="av"
if x is y:
    print("yes")
else:
    print("np")