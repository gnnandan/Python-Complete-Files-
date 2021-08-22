# creating a empty dictionary
dic={}
print(f"Empty dictionary {type(dic)}")

# creating a dictionary
# key can be int or strings
# values can also be int or strings
dic={'Nandan':'CSE','Yashas':'ME','Ganesh':'ME','Pavan':'CSE'}
print(f"The dictionary is: {dic}")

# creating a dictionary within dictionary(Nested Dictionary)
data={"Name":{"first_name":"Nandan","last_name":"G N"},"age":23,"Branch":"CSE"}
print(data)

print()
#creating a dictionary using from
keys=('a','b','c','d','e','f')
values='Nandan'
new_dict=dict.fromkeys(keys,values)
print("The new dictionary using 'fromkeys'",new_dict)