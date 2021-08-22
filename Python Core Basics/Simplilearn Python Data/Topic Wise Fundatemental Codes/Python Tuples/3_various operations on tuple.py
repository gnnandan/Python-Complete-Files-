# creating a tuple
x=("Bangalore","Mysore","Tiptur","Tumkur")
y=("Shivamogga","Coimbatore")

print()
# concatenating tuples
new_tuple=(x+y)
print(f"The tuple after the concatenation '{new_tuple}'")

print()
# Nesting a tuple
nest_tuple=(x,y)
print(f"The tuple after the nesting '{nest_tuple}'")

print()
# repetition of tuples
rep_tuple=('100',)*10
print(f"The tuples after repetition '{rep_tuple}'")

print()
# slicing the tuples
x=("Bangalore","Mysore","Tiptur","Tumkur")
print(f"The tuples after slicing '{x[2:3]}'")

print()

# reversing the tuples
x=("Bangalore","Mysore","Tiptur","Tumkur")
print(f"The reversed order of the tuple '{x[::-1]}'")

print()

# unpacking the tuples
x=("Bangalore")
print(f"The unpacking of tuple x is '{tuple(x)}'")
print()

# holding tuple one by one seprate variables
x=("Bangalore","Mysore","Tiptur","Tumkur")
a,b,c,d=x
print("Holding tuple values one by one order in seperate variables")
print(a)
print(b)
print(c)
print(d) 

print()
# holding tuple values one by one seprate variables when we don't know how much values we have
print("Holding tuple values one by one order when don't know the number of values in tuple")
x=("Bangalore","Mysore","Tiptur","Tumkur")
a,*b,c=x
print(a)
print(b)
print(c)

print()
# deleting the tuple values using del()
# x=("Bangalore","Mysore","Tiptur","Tumkur")
# del(x)
# print(f"after deleting the tuple '{x}'")
## "output" NameError: name 'x' is not defined