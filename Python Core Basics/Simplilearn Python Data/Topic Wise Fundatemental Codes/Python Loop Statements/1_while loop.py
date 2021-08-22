def while_ex(a):
    times=0
    while times < 10:
        times+=1 # Note increment use here!
        print(f"{times} : {a}")



a=input("Enter what to print 10 times: >>")
while_ex(a)