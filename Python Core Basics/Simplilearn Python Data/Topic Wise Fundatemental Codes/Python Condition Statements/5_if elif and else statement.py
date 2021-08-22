def elif_ex(a):
    if a > 0:
        return(f"{a} is a positive number")
    elif a == 0:
        return(f"{a} is equal to 0")
    elif a < 0:
        return(f"{a} is negative number")
    else:
        return (f"{a} is invalid")

a=int(input("Enter a: >> "))
print(elif_ex(a))