# necessary Variables
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

# function
def Calculator(op):
    if op == 1:
        print("You choose Addition",num1 + num2)
    elif op == 2:
        print("You choose Subtraction",num2 - num1)
    elif op == 3:
        print("You choose Multiplication",num1 * num2)
    elif op == 4:
        print("You choose Division",num1 / num2)
    elif op == 5:
        print("You choose Power",num1 ** num2)
    elif op == 6:
        print("You choose Floor Division",num1 / num2)
    elif op == 7:
        print("You choose Modulus",num2 % num1)
    else:
        print("Invalid Input")
    
# operations
op={1:'add',2:'sub',3:'mul',4:'div',5:'power',6:'floor',7:'modulus'}
op=int(input("Enter op no:"))
Calculator(op)
    
    
    
    
