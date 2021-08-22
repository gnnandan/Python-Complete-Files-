a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))
if a == b:
    print("{} and {} are equal".format(a,b))

elif a > b:
    print("{} is greater than {}".format(a,b))
    
elif a < b:
    print("{} is lesser than {}".format(a,b))
else:
    print("invalid")
    