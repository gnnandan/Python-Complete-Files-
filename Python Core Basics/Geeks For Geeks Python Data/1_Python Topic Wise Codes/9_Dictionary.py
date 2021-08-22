data={'Nandan':1,'Yashas':8,'Ganesh':3,'Pavan':12,'NotApplicable':None,'pop':'No'}
print("This is **{}**".format(type(data)),"and items are **{}**".format(data))

# accessing 
print("access using key",data['Nandan'])

# access using get key
print("access key data using get()",data.get('Nandan'))
if "Nandan" in data:
    print(data['Nandan'])
else:
    print("NA")
    
# operations
print("length of dictionary",len(data))
print("\n")
data['Nandan']=7
print("We can change the existing data",data)

print("\nRemoving the element **{}**".format(data.pop('NotApplicable')),"The remaining elements are **{}**".format(data))

del data['pop']
print("\nThe remaining elements are **{}**".format(data))
print("\n")
data['Hari']=10
print("\nAfter inserting 'Key:Value' the remaining elements are **{}**".format(data))

print("\npop.item() removes last item",data.popitem(),"the remaining elements are **{}**".format(data))