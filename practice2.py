n=int(input("enter any number"))
mn=int(input("enter any starting range"))
mx=int(input("enter any last range"))

for i in range(mn,mx+1):
    if n%i==0:
        print(f" {i}is the divisor of {n}")
    else:
        print(f" {i}is not the divisor of {n}")
if mn==mx:
    raise ValueError("range is not defined")
elif mn>mx:
    raise ValueError("select valid range ")








