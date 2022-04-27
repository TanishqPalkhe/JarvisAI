def addition(a, b):
    print(a + b)


addition(6, 8)


def subtract(a, b):
    return a - b


print(subtract(8, 7))


def fun1(a, b, c):
    return (a + b + c) / 3


print(fun1(4, 6, 9))
# faulty calculator
user_input = input("chosse any operator")
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
if user_input == '+' and num1 == 56 and num2 == 6:
    print(59)
else:
    print(num1 + num2)
num1 = input("enter first no")
num2 = input("enter second no")
try:
    print(int(num1) + int(num2))
except Exception as w:
    print(w)
print("you win")

