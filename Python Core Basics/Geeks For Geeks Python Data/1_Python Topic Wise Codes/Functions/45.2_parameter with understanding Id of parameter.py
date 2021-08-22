def fun(x):
    print("The initial memory address of x",id(x))
    x=10
    print("Memory adderess of x (Local Variable)",id(x)) 
    
x=100000
print("Memory adderess of x (Global Variable)",id(x))
fun(x)