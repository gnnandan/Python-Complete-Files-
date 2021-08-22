# logical operator for string and boolean
s1=str(input("Try with 'empty string' and with also some value:"))
s2= s1 or "Im inserted"
print(s2)
"""
[Explanation]
or operator checks 
if s1 is empty then data "Im inserted" is inserted into
else prints s1
"""
l=[]
s2=l or ["Container Data is added"]
print(s2,type(s2))