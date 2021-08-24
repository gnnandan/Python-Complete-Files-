def add(a,b):
    a = 1.0
    b = 2.0
    print(f"Second Call Memory address of {a} = {id(a)} and {b} = {id(b)}:")
    sum = a+b
    print(f"The sum of {a} and {b} is {sum}")

a = 100
b = 200
print(f"First Call Memory address of {a} = {id(a)} and {b} = {id(b)}:")
add(20,30)
