"""
["Statement"]

Given two inputs that are stored in variables a and n, 
you need to print a n-times in a single line 
separated by space.


[Output should be]

Input:
a = "Hello"
n = 5
Output: 
Hello Hello Hello Hello Hello
Explanation: a is printed n=5 times in a single line 
seperated by space between them.

"""

a=str(input("Enter string 1:"))
n=int(input("Enter number for times need to repeat:"))
res=a+' '
print(res*n)