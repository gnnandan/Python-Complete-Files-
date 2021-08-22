# identity comparision operator
"""
[Check]
give a and b with the same input and check
give a and b with the different input and check
"""
a=int(input("Enter a:"))
b=int(input("Enter b:"))
if a is b:
    print("equal:",a is b)
elif a is not b:
    print("not equal:",a is not b)
    
