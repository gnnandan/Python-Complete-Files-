# creating an empty dictionary
d={}

# adding elements to the dictionary
d[0]="Nandan"
# or d['name']="Nandan" (you can also give 'String' as a keyname)
print("after adding 1 element:",d)
print()
d[1]=("Yashas","Ganesh"),"Pavan"
print("after adding another element:",d)

# adding a nested dictionary
d['Name']={"first_name":"Nandan","last_name":"G N"}
print("after adding a nested dictionary:",d)