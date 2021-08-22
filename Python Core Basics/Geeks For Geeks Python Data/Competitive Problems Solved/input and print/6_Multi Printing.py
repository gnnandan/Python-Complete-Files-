"""
["Statement"]

Given two inputs that are stored in variables a and n, 
you need to print a, n 
times in a single line without space between them.


[Output should be]

Input:
a = "Hello"
n = 5
Output: 
HelloHelloHelloHelloHello

Explanation: 
a is printed n=5 
times in a single line without space between them.

"""

a=str(input("Enter string 1:"))
n=int(input("Enter number for times need to repeat:"))
print(a*n)