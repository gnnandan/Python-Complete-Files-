def var_ex():
    # Note variable should be use only with in the scope of method
    a="local variable 1"
    b="local variable 2"
    print(f"Variables {a,b,c,d}")
    
c="Global variable 1"
d="Global variable 2"
print(c,d)
print(var_ex())