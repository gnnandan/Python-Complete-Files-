"""
The function sum_positive_numbers should 
return the sum of all positive numbers between 
the number n received and 1. For example, 
when n is 3 it should return 1+2+3=6, 
and when n is 5 it should return 1+2+3+4+5=15.
Fill in the gaps to make this work:"""

def sum_positive_numbers(n):
    if n < 1:
        return n
    
    return n+sum_positive_numbers(n-1)

print(sum_positive_numbers(3))
print(sum_positive_numbers(5))