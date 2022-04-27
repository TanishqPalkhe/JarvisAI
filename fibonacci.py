name = "tanishq"
for item in name:
    print(item)
d = [["carry", "golf"], ["marry", "criket"], ["tanishq", "chess"]]


# fibonacci series
# 011235813......n
def factorial(n):
    p = 1
    for i in range(n):
        p = p * (i + 1)
    return p


user_input = int(input("enter any number"))
print(factorial(user_input))


def fibonacci(n):
    a = 0
    b = 1

    if n == 1:
        return a
    elif n == 2:
        return (a, b)
    else:
        print(a, b, end=" ")
        for i in range(n - 2):
            c = a + b
            a = b
            b = c
            print(b, end=" ")


user = int(input("enter a number"))
print(fibonacci(user))


def person(name, age, number):
    print(name)
    print(number)


person("tanishq", 74, 698988090769)


def funargs(normal, *argsrohan, **kwarg):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwarg.items():
        print(f"{key} is a {value}")


har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)
# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)
l1 = ["tp", "aloo", "loki", "muli"]
for lom, item in enumerate(l1):
    if lom % 2 == 0:
        print(item)

#
n = int(input("enter"))
c = ((n - 32) * 5) / 9
print(f"temperature in celcius{c}")
m = int(input("enter columns"))
n = int(input("enter rows"))


def matrics(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = input(f"p{i}{j}")
            row.append(inp)
        o.append(row)
    return o


A = matrics(m, n)
print(A)

B = matrics(m, n)
print(B)


def sum(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output
print(sum(A, B))
