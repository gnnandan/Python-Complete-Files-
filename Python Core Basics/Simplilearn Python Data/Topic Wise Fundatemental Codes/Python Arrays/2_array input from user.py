from array import *

array = array('i',[])
x = int(input("enter the size of array:"))
print(f"Enter {x} elements one by one:")

for i in range(x):
    n = int(input())
    array.append(n)
print(array)