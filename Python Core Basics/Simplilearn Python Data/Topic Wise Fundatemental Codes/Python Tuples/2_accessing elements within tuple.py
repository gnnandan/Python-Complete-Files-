# creating a tuple
x=("Bangalore","Mysore","Tiptur","Tumkur")
#    0             1      2        3  NOTE positive index
#    -4            -3     -2       -1 NOTE negative index
print(f"This is {type(x)}")

# accessing the tuple 
print(f"accessing tuple using positive index '{x[1]}'")
print(f"accessing tuple using negative index '{x[-1]}'")
print(f"accessing tuple using positive index '{x[3]}'")
print(f"accessing tuple using negative index '{x[-3]}'")

print()
# accessing the tuple using range indices
# positive
print(f"accessing tuple using positive ragne(:) indices '{x[0:]}'")
print(f"accessing tuple using positive ragne(:) indices '{x[0:2]}'")
print(f"accessing tuple using positive ragne(:) indices '{x[2:3]}'")
# negative
print(f"accessing tuple using negative ragne(:) indices '{x[:-1]}'")
print(f"accessing tuple using negative ragne(:) indices '{x[-2:-1]}'")
print(f"accessing tuple using negative ragne(:) indices '{x[-4:-2]}'")

print()

# reversing the tuple values
print(f"before reversing the tuple values '{x}'")
print(f"after reversing the tuple values '{x[::-1]}'")