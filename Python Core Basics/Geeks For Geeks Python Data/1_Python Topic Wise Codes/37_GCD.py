# Note
"""
[summary]
GCD==> Greatest Common Divisor
algorithm

- check for small numbers in both using min()
- loop from 1 to small and find the last number that divides both 'a' and 'b'

"""
a=int(input("Enter the size of a:"))
b=int(input("Enter the size of b:"))
small=min(a,b)
for i in range(1,small+1):
    if(a % i == 0) and (b % i == 0):
        gcd=i
print("Largest number that divides {} and {} is {}".format(a,b,gcd))