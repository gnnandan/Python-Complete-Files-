# creating the string
var="""hi i'm Nandan G N
Hope, you are doing well"""

# accessing the string
print(f"accessing the single character: {var[10]}")
print(f"accessing the range of character:{var[0:10]}")
print()

# extracting the sequence of characters
for c in var:
    # print(c) try by only c
    print(c,end=",") # extracting in a sameline
print()  

# extracting a part of string
print(f"extracting a part of string: **{var[7:20]}**")
print()

# reversing the strings
print(f"reversed string: **{var[::-1]}**")