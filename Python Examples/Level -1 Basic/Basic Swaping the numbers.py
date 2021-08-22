def swap(a,b):
    # logic
    print("Before swap",(a,b))
    temp=a
    a=b
    b=temp
    print("After swap",(a,b))
a=int(input("Enter a:"))
b=int(input("Enter b:"))
swap(a,b)

a,b=b,a
print("You can swap like this also a,b=b,a:({},{})".format(a,b))