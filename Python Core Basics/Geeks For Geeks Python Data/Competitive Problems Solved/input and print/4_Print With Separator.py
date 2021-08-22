"""
["Statement"]

You'll be given two strings a and b, 
a separator symbol, and you need to print a and b 
such that a and b are separated by the separator symbol.


[Output should be]

Input:
a = "Hello"
b = "World"
separator = "@"
Output: 
Hello@World
Explanation: a and b are printed
with the separator symbol in between.
"""

a=str(input("Enter string 1:"))
b=str(input("Enter string 2:"))
separator=str(input("Enter symbol:"))
print(a,b,sep=separator)