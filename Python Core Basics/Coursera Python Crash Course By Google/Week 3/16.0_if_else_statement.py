# example companey name authentication

name=input("Enter your name: ")
if len(name) < 2:
    print(name,"INVALID....")
else:
    print(name,"VALID Done You Are IN....")
    
# OR

def chk_empname(name):
    if len(name) < 2:
        return ("INVALID....")
    return print("Valid....") ### Here is the Tricky CODE)
chk_empname(name)
name=input("Enter your name: ")