# list
num=[1,2,3,4,5,6,7]

# append()---->num.append(data to add) used to add element at the end of the list
num=[1,2,3,4,5,6,7]
num.append(8)
print("list num after appending:",num)

print()

# extend()---->num.extend(list of data) used to add another list at the end of the list
num=[1,2,3,4,5,6,7]
alpha=['a','b','c','d','e','f']
num.extend(alpha)
print(f"list after extending: {num}")

print()

#insert()--->elements.insert(index,data to add) used to insert element in any position in the list
elements=[1,2,3,4,5,6,7]
elements.insert(3,"i inserted in middle")
print(f"list after extending: {elements}")

print()

#remove() ---->elements.remove(data) used to removes the first occurance of the perticulat element
elements=[1,1,2,3,1,4,4,5,6,7]
elements.remove(1)
print(f"list after removing the first occurance of the perticulat element {elements}")

print()
#sort() ---->elements.sort() used to removes the first occurance of the perticulat element
alpha=['a','c','b','x','z','y','n','A','C','D','N','Z']
integer=[-1,1,0,100,-1000,1.2,-1.2,300,-300]
alpha.sort()
integer.sort()
print(f"list after sorted 'alpha {alpha}' || 'integer {integer}'")