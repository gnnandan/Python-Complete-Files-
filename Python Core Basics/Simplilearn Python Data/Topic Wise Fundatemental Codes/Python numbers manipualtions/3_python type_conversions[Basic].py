# checking data type before conversion
for i in (1,1.1,'a',True,(1,2,3,4,5,6),[1,2,3,4,5,6,7,8],{1:'one',2:'two'},{1,2,3,4,5,6}):
    print(type(i))
    
# converstion
print("\n######| Conversion Shown Below |######")

# int to float
a=10
print("\nBefore conversion:",a,type(a),"|<--->|","After conversion",float(a),type(float(a)))

# int to complec
a=10
print("\nBefore conversion:",a,type(a),"|<--->|","After conversion",complex(a),type(complex(a)))
print("OR")
print("You can create a complex number like this also:",complex(100,200))

# int to string
a=10
print("\nBefore conversion:",a,type(a),"|<--->|","After conversion",str(a),type(str(a)))

# int to bool
a=10
print("\nBefore conversion:",a,type(a),"|<--->|","After conversion",bool(a),type(bool(a)))

# tuple to list
a=(10,20)
print("\nBefore conversion:",a,type(a),"|<--->|","After conversion",list(a),type(list(a)))

# tuple to dictionary
a=((10,'Ten'),(20,'Twenty'))
print("\nBefore conversion:",a,type(a),"|<--->|","After conversion",dict(a),type(dict(a)))

# tuple to set
a=((10,'Ten'),(20,'Twenty'))
print("\nBefore conversion:",a,type(a),"|<--->|","After conversion",set(a),type(set(a)))

