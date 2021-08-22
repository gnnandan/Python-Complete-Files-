"""
[Statement]
A person gets 5000 salary on 1st august 2020.
The salary increases by 2000 every month.
Find the salary that the person is going to get on 1st August 2025.

[Formula]
nth-term=a+(n-1)d
a=first-term
d=common difference 
n=total months
"""
a=5000 # first term
n=61   # total number of month
d=2000
sal=a+(n-1)*d
print("The salary that the person is going to get on 1st August 2025 is:",sal)