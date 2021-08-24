# note 
# ! when we dont know how much parameter that user gives then we use "*args"
def add(*a):
    # ! when we use *args the return statement is list so 
    total = 0
    for i in a:
        total = total + i
    print(f"The sum is: {total}")

add(10,20,30,40,50,60,70)