l=[1,1.1,'1','Hello',True]
print(l)

# accessing list using index
print("Positive indexing:",l[1])
print("Positive indexing:",l[4])
print("\n")
print("Negative indexing:",l[-1])
print("Negative indexing:",l[-5])

# more fuctions "Insert and search"
l=[10,20,30,40,50,20]

#"append"=Append object to the end of the list.
l.append(60)
print(l)

print("\n")

# check if item in list 
inp=int(input("Enter the item to check if present or not:"))
print("The item {} is present so:".format(inp),inp in l)

inp=int(input("Enter the item:"))

# count the number of items in the list
print("\n")
print("counts the number of item is present",l.count(inp))

# check the index first occurance of item
print("\n")
print("index of {} is:".format(inp),l.index(inp))

# removing the items
l=[10,20,30,40,50,20]
print("removes the given item:",l.remove(10),l)

# pop gives returned value
print("pops the element from last for given specified number:",l.pop(2),l)

# del general purpose keyword used to delete the specified
print("\n")
del l[0]
# specifing range 
del l[0:1]
print(l)

# general purpose functions
l=[0,10000,235,44,5,1.1,-100000,100,-2,3,-1,1,0.1,300]
print("max item in l:",max(l))
print("min item in l:",min(l))
print("reverse of l:",l.reverse(),l)
print("sorted list is:",l.sort(),l)