"""
[Syntax]
if condition:
    // execute the if part of statements
elif:
    // execute the elif part of statements
else:
    // execute else part of statements
"""
num=int(input("Enter the num:"))
if num > 0 and num % 2 == 0:
    print ("{} positive even number".format(num))
elif num < 0 and num % 2 == 0:
    print(("{} negative even number".format(num)))
        
elif num > 0 and num % 2 != 0:
    print ("{} positive odd number".format(num))
        
elif num < 0 and num % 2 != 0:
    print ("{} negative odd number".format(num))
    
else:
    num ==0
    print(("{} is equal to zero".format(num)))
