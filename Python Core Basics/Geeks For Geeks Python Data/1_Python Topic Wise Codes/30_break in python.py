"""
[Question]
find the smallest divisor of a number 
such that the divisor is greater than 1

[Algorithm]
- take n inputs
- run looop from x=2 to n+1
    -if n%x==0 print x and break
"""

n=int(input("Enter number: "))
for x in range(2,n+1):
    if n % x == 0: #note 
        print("The smallest divisor of {} using for loop is".format(n),x)
        break
    
x=int(input("Enter x:"))
while x <= n:
    if n % x == 0: #note 
        print("The smallest divisor of {} using while loop is".format(n),x)
        break
    x+=1
