"""
["Statement"]

Given four inputs that are stored in variables a, b, c, and d. 
you need to print three arrows made up of a ,
vertical distance between all three arrows will be length b, 
the middle arrow will be forward by a horizontal distance of length c. 
length of the arrow will be d (body) plus 1 for the tip.

[Output should be]

a = '-'
b = 3
c = 10
d = 15

Output:
--------------->


          ----------->


--------------->
Explanation:
The body of the arrow is made up of a.
The length is (d = 15(body))+1(tip).The vertical distance is b = 3, 
and the middle arrow start with the horizontal distance of c = 10.
"""
a=input("Enter Symbol:")
b=int(input("Enter b distance:"))
c=int(input("Enter c distance:"))
d=int(input("Enter d distance:"))

verDist = '\n' * b

print(a * d, '>', sep='', end=verDist)
print(' ' * c,a*d, '>', sep='', end=verDist)
print(a*d, '>', sep='')