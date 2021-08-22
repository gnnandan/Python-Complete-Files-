# multiplating the list elements 
x=["HUMANITY"]*10
print(x)


print()
# concatenating{Joining} the list elements
x=["HUMANITY"]
y=["should be the religion of HUMANS"]
print(f"{x+y}")

# unpacking the list elements
print()
y=["HUMANITY","should be the religion of","HUMANS"]
one,*other=y #note '*' helps to do this 
print(one)
print(other)