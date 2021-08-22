# Note
"""
[Algorithm]


logic n*(n-1)!
fact =fact * n
"""
num=int(input("Enter num to find factorial:"))
fact=1
for n in range(2,num+1):
    fact=fact * n
print ("Factorial of {} is:".format(num),fact)