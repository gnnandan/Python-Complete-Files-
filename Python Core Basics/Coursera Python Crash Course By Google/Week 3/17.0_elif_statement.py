def chk_emp(name):
    if len(name) < 3:
        print(name,"Try again...")
    elif len(name) > 10:
        print(name,"Once again.....")
    elif len(name) == None:
        print(name,"Please enter valid one:")
    else:
        print(name,"VALID Done You Are IN....")

name=input("Enter your name: ")
chk_emp(name)
