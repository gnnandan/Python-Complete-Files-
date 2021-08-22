# creating a empty dictionary
d={}

# adding element to the empty dictionary
d["name"]={"first_name":"Nandan","last_name":"G N"}
d["age"]=23
d["email"]="gnnandan7@gmail.com"
d["branch"]="CSE"
d["Null"]="NULL"
d["0"]="0"

print("after adding element to dictionary:",d)
print()

# accessing the dictionary
print("accessing one element",d["name"])
print("accessing elements by using 'get': ",d.get("email"))

print()

# accessing the desired parts
print("getting only keys:",d.keys())
print()
print("getting only values:",d.values())
print()
print("getting only items:",d.items())

print()

# deleting the element
print("Deleting element using 'pop()':",d.pop("Null"))
print("after deleting",d)

print()

print("Deleting element using 'popitem()':",d.popitem())
print("after deleting",d)