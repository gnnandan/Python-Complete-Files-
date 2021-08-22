"""
["Statement"]

Given two inputs that are stored in variables a and n, 
you need to print two horizontal lines made up of a. 
First-line will be of length n, and 
Second-line length will be double of the first line.

[Output should be]

a = "#"
n = 10
Output: 
##########
####################
Explanation: Printed first Line of length n=10 and second Line of length 2*10=20.
"""

a=str(input("Enter string :"))
n=int(input("Enter number for times need to repeat:"))
res=a*n
print(res)
print(res+a*n)