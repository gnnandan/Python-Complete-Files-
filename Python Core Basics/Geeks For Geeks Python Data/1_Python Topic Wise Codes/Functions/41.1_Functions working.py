def func2():
    print("Inside function 2()")
    
def func1():
    print("Before function 2()")
    func2()
    print("After function 2()")
    
# main codes
print("Before function 1()")
func1()
print("After function 1()")