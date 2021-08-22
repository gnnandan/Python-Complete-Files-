# conversions
# checking type
for i in (1,1.1,'a',True,(1,2,3,4,5,6),[1,2,3,4,5,6,7,8],{1:'one',2:'two'},{1,2,3,4,5,6}):
    print(type(i))
    
# converstion
print("\nConversion")

# int to float
a=10
print("before conversion:",a,type(a),"after conversion",float(a),type(float(a)))

# int to string
a=10
print("before conversion:",a,type(a),"after conversion",str(a),type(str(a)))

# int to bool
a=10
print("before conversion:",a,type(a),"after conversion",bool(a),type(bool(a)))

# tuple to list
a=(10,20)
print("before conversion:",a,type(a),"after conversion",list(a),type(list(a)))

# tuple to dictionary
a=((10,'Ten'),(20,'Twenty'))
print("before conversion:",a,type(a),"after conversion",dict(a),type(dict(a)))

# tuple to set
a=((10,'Ten'),(20,'Twenty'))
print("before conversion:",a,type(a),"after conversion",set(a),type(set(a)))

