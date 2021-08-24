# Syntax
# ! var = Array(TYPE CODE,[elements])

from array import *
data = array('i',[1,2,3,4,5,6,7])

print("elements of array is:",data) 
print()


print("accessing the element:",data[2])
print()


print("Iteration on array")
for el in data:
    print(el)
print()


print("position and element")
for pos in range(0,len(data)):
    print(f"In position {pos}, the element is: {data[pos]}")
print()

print("revercing array")
print(f"Before revercing {data}")
data.reverse()
print(f"after revercing {data}")
print()

print("appending element to array")
data.append(10000)
print(data)
print()

print("removing element from array")
data.remove(10000)
print(data)
print()


print("printing the index of element from array")
print("The index is of 4 is:",data.index(4))
print()