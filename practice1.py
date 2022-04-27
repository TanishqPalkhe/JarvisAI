user=int(input("enter your age and year of birth"))
if len(str(user))==3:
    if user>=100:
        raise ValueError("you are the oldest person alive")
if len(str(user))==2:
    if user<100:
        r=int(input("enter your year of birth"))
        if r >= 2022:
            raise ValueError("you are not yet born")
        elif 1000 < r < 2022:
            print(f"you will be 100 years old after {100 + r} year amd after {100-user}")
            e=input("press yes or no to proceed")
            if e=="yes":
                p = int(input("enter any year to know your date of birth"))
                r = int(input("enter your year of birth"))
                if p < r:
                    raise ValueError("you are not born at that time")
                elif p > r:
                    print(f"your age in {p} will be {p - r}")
                else:
                    print("you are born in this year")
            else:
                exit()
    else:
        print("invalid")
if len(str(user))==4:
    if user>=2022:
        raise ValueError("you are not born yet")
    elif user<2022:
        print(f"you will be 100 years old after {100 + user} year")

        p = int(input("enter any year to know your date of birth"))
        r = int(input("enter your year of birth"))
        if p < user:
            raise ValueError("you are not born at that time")
        elif p > user:
            print(f"your age in {p} will be {p - user}")
        else:
            print("you are born in this year")
    else:
        print("invalid")











