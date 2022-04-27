import random
a=int(input("enter a"))
b=int(input("enter b"))
total=random.randint(a,b)
print("Player1")
for i in range (0,10):
    user=int(input(f"guess a number between {a} and {b}"))
    if user==total:
        trial1=i+1
        print(f"you win and no of trials you take {trial1}")
        break
    elif user>total:
        print("you made a high guess lower")
    else:
        print("you made a low guess guess high")

print("Player2")
total1=random.randint(a,b)
for i in range (0,10):
    user1=int(input(f"guess a number between {a}and {b}"))
    if user1==total1:
        trial2 = i+1
        print(f"you win and no of trials you take {trial2}")
        break
    elif user1>total1:
        print("you made a high guess lower")
    else:
        print("you made a low guess guess high")

if trial1==trial2:
    print("game is draw")
elif trial1>trial2:
    print("player2 is win the match")
else:
    print("Player1 win the match")




