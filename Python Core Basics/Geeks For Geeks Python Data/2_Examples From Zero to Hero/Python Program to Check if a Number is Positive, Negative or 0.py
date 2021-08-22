def num(a):
    if a == 0:
        print("The number {} is equal to 0".format(a))
    elif a < 0:
        print("The number {} is negative".format(a))
    elif a > 0:
        print("The number {} is positive".format(a))
    else:
        print("Invalid")
        
a=int(input("Enter num:"))
num(a)