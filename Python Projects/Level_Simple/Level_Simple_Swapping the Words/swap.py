def swap(a,b):
    print(f"before swap a:b >> {a} {b}")
    
    # Note actual logic
    temp=a
    a=b
    b=temp
    print(f"after swap a:b >> {a} {b}")
    
a="Hello,"
b="World!"
swap(a,b)