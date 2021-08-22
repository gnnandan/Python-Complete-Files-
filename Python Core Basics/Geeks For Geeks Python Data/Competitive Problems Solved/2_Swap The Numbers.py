def swap(a,b):
    # operation
    temp=a
    a=b
    b=temp
    print("after swapping:",a,b)
    
a=int(input("enter a:"))
b=int(input("enter b:"))
swap(a,b)