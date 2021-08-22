x=[1,2,'a','b','aa1','bb2']

print(f"Before conversion list x is '{type(x)}'")
x=tuple(x) #NOTE
print(f"After conversion list x is '{type(x)}'")

# nesting tuple inside the list
x=[(1,2),('a','b','aa1','bb2')]
print(f"{x} and {type(x)}")

# tuple is immutable but list is mutable we can add n number of tuple in the list
x=[(1,2),('a','b','aa1','bb2')]
x.append(("Added","Inside","Existing","List","Using","tuple"))
print(x,type(x))

print()
x.remove((1,2))
print("The list after removing ",x)
print()

#nesting list inside the tuple
x=(["Tiptur","Mysore"],["Bangalore","Tumkur"])
print(f"{x} and {type(x)}")

print()
# adding data insite the list of tuples
x[0].append("Nandan") #Note
print(f"After adding data insite the list of tuples {x}")

print()
# adding another list inside the list fo tuple
x[1].append(['Hello',"Good"])
print(f"After adding another list inside the list fo tuple {x}")