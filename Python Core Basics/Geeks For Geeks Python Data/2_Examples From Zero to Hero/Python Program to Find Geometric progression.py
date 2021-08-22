"""
[Statement]
A person gets 5000 salary on 1st jan 2020.
The salary doubles every year.
Find the salary that the person is going to get on 1st jan 2030.

[Formula]
n-th term of geometric progression is a*r**n-1
"""
a=5000
r=2   #doubles every year
n=11  #years

sal=a*r**(n-1)
print("The salary that the person is going to get on 1st jan 2030:",sal)