user_input=int(input("enter number of rows"))
op= input("press 1 for true and 0 for false")
if op=="1":
    for i in range (0,user_input+1):
            print("*"*int(i))
if op=="0":
    for i in range (user_input,0,-1):
            print("*"*int(i))
    # snake water gun
import random
list1=['snake','water','gun']
i=0
while i<10:
    a = random.choice(list1)
    guess = input("enter s for snake w for water and g for gun")
    if guess=="s"and a=="water":
        print(f"your is {guess}and computer has {a}")
        i+=1
        print("you win")
    elif guess=="s"and a=="gun":
        print(f"your is {guess}and computer has {a}")
        i+=1
        print("you loose")
    elif guess=="g"and a=="water":
        print(f"your is {guess}and computer has {a}")
        print("you loose")
        i+=1
    elif guess=="g"and a=="snake":
        print(f"your is {guess}and computer has {a}")
        print("you win")
        i+=1
    elif guess=="w"and a=="snake":
        print(f"your is {guess}and computer has {a}")
        print("you loose")
        i+=1
    elif guess=="w"and a=="gun":
        print(f"your is {guess}and computer has {a}")
        print("you win")
        i+=1
    else:
        print("draw")












