# caluclator arithmetic operation
# Remember the method
import sys
import math

# Note This is special method to take the input from prit statement 
print
(""""Enter the choise below from 
1.add
2.sub
3.multiplication
4.division
5.Modulus
6.floor_division
7.square
8.sqrt
9.sin
10.cos
11.tan
""")

# take inputs 
sel=int(input("Enter the choise from 1 to 11="))
a=int(input("Enter num1="))
b=int(input("Enter num2="))

# check for exist or not
if sel not in(1,2,3,4,5,6,7,8,9,10,11):
    sys.exit()

# build logic 
if sel == 1:
    print("The sum {} and {} is".format(a,b),a+b)

elif sel == 2:
    print("The difference {} and {} is".format(a,b),b-a)

elif sel == 3:
    print("The product {} and {} is".format(a,b),a*b)

elif sel == 4:
    print("The ratio {} and {} is".format(a,b),a/b)

elif sel == 5:
    print("The modulus {} and {} is".format(a,b),a%b)

elif sel == 6:
    print("The floor_division {} and {} is".format(a,b),a//b)

elif sel == 7:
    print("The square {} over {} is".format(a,b),a**b)

elif sel == 8:
    print("The square root of {} is".format(a),math.sqrt(a))

elif sel == 9:
    print("The sin of {} is".format(a),math.sin(a))
    
elif sel == 10:
    print("The cos of {} is".format(a),math.cos(a))

elif sel == 11:
    print("The tan of {} is".format(a),math.tan(a))
    
def special_types(a,b):
    print("The absolute value of {} and {} is==>".format(a,b),abs(a),"and",abs(b))
    print("The conjugate of {} and {} is==>".format(a,b),a.conjugate(),"and",b.conjugate())
    print("The diffrence '% and //'==>".format(a,b),a%b,"and",a//b)

a=int(input("Enter a:"))
b=int(input("Enter b:"))
special_types(a,b)