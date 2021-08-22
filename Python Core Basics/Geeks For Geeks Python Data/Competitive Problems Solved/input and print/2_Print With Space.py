"""
["Statement"]

Given two inputs that are store in variables a and b,
you need to print a and b 
in a single line with a space separating them.

[Output should be]

Input:
a = "Hello"
b = "World"
Output: 
Hello World
Explanation: a and b are printed in a
single line and a space separates them.
"""
a=str(input("Enter string 1:"))
b=str(input("Enter string 2:"))
print(a,b,sep=' ')