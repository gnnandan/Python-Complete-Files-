# set
s1={'Nandan','Yashas','Ganesh','Pavan'}
print("This is {}".format(type(s1)),"values are {}".format(s1))

# insertion in set
# add()
s1.add('Hari')
print(s1)

# update
print("\n")
s2=['Tiptur','Bangalore']
s1.update(s2)
s1.update(['Tiptur','Bangalore'],['Tumkur','Karnataka'])
print("Updated set is:",s1)

# removal
print("\n")
s1.discard('Karnataka')
print("after discard {}".format(s1))
s1.remove('Tiptur')
print("\nafter removal of element {}".format(s1))
s1.clear()
print("\nafter clearing set {}".format(s1))

# del s1 #completly wips the set
# print("after del {}".format(s1))
s1.update([10,20,30,40,50])
# operation on set
print("Set is {}".format(s1))
print("\nChecking the length of the set **{}**".format(s1))
print("\nChecking an item is present in the set **{}**".format(10 in s1))

# operations on 2 set
s1={10,20,30,40,50}
s2={10,20,30,40,50,60}

print("Union of set **{}**".format(s1 | s2))
print("intersection of set **{}**".format(s1 & s2))
print("Difference of set **{}**".format(s2 - s1))
print("Symmetric Difference of set **{}**".format(s1 ^ s2))
print("disjoint set **{}**".format(s1.isdisjoint(s2)))
print("subset of set **{}**".format(s1 <= s2))
print("proper subset of set **{}**".format(s1 < s2))
print("super set **{}**".format(s1 >= s2))
print("proper super set **{}**".format(s1 > s2))