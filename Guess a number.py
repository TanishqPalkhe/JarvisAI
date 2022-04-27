def addition(a,b):
    print(a+b)
addition(6,8)
def subtract(a,b):
    return a-b
print(subtract(8,7))
def fun1(a,b,c):
    return (a+b+c)/3
print(fun1(4,6,9))
#faulty calculator
user_input= input("chosse any operator")
num1= int(input("enter first number"))
num2= int(input("enter second number"))
if user_input=='+'and num1==56 and num2==6:
    print(59)
else:
    print(num1+num2)
    n = 30
    no_of_guesses = 0
    while (no_of_guesses < 10):
        i = int(input("Enter your guess: "))
        if i == n:
            print("Your guess is correct!")
            break
        elif i > n:
            print("Your guess is too big, guess something smaller!")
            no_of_guesses = no_of_guesses + 1
            print("Guess left: ", {10-no_of_guesses})
            continue

        elif i < n:
            print("Your guess is too small, guess something bigger!")
            print("Guess left: ",{no_of_guesses})
            no_of_guesses = no_of_guesses + 1
            continue

    print("Game Over")


































