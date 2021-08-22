# Note
"""
when we use for loop to check for all divisors it will take large amount of processing speed and time.
so we use this optimizing technique to overcome this effect
"""
import math
n=int(input("Enter number:"))
x=1
while x*x < n:
    if n % x == 0:
        print(x)
        # print(n//x)
    x=+1
if x*x  == n:
    print(x)
    