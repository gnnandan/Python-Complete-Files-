t=(0,10,100, 1000,10000)
print("This is {} and the items are:".format(type(t)),t)

# accessing tuple
# indexing
print("positive index:",t[1])
print("Negative index:",t[-1])

# slicing
print("\nSlicing using positive index:",t[0:2])
print("Slicing using negative index:",t[-3:-1])

print("\nThe length of tuple is:{}".format(len(t)))

