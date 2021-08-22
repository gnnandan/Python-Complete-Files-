def nested_if_else(a):
    if a > 0:
        if a > 20:
            print("Positive side")
            return(f"{a} is greater than 20")
        else:
            print("Positive side")
            return(f"{a} is not greater than 20")
    else:
        if a < 0:
            if a > -20:
                print("Negative side")
                return(f"{a} is greater than -20")
            else:
                print("Negative side")
                return(f"{a} is leaster than -20")
                
a=int(input("Enter a: >>"))
print(nested_if_else(a))
