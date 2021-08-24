def if_else_ex(a):
    if a > 20:
        print(f"{a} is greater than 20")
        return("inside the if statement because 'if statement is True'")

    else:
        print(f"{a} is lesser than 20")
        return("inside else block because the 'if condition False'")
    
a=int(input("Enter a >>"))
