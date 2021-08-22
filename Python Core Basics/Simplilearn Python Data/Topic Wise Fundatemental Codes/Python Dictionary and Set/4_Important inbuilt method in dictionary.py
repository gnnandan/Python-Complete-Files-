# creating a new dictionary
d={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven"}

# printing only values
print(f"values: {d.values()}")
print(f"keys: {d.keys()}")

print()

#creating a dictionary using from
keys=('a','b','c','d','e','f')
values='Nandan'
new_dict=dict.fromkeys(keys,values)
print("The new dictionary using 'fromkeys'",new_dict)

# using clear method to clean the dictionary
print(f"after clearing the dictionary {new_dict.clear()},'{new_dict}'")