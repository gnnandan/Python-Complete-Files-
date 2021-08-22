def func(x):
    x="This is local variable"
    print(x)
    
x="Global variable" 
func(x)
print(f"The value of x is '{x}'")
