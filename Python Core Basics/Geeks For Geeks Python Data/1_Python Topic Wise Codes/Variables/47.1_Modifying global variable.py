def var_ex():
    # Note variable should be use only with in the scope of method
    a="local variable 1"
    b="local variable 2"
    c=100 # Modifying the global variable
    d=10000 # Modifying the global variable
    print(f"Variables {a,b,c,d}")
    
c="Global variable 1 **100**"
d="Global variable 2 **1000**"
print(c,d)
print(var_ex())