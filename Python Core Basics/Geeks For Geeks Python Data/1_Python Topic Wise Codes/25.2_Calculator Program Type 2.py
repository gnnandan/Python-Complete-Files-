import sys
print
("""Please select an Operation:
1.Add
2.Sub
3.Mul
4.div
5.mod
6.power
7.floordiv
""")
choice=int(input("Select any of the operation from above:"))

if choice not in (1,2,3,4,5,6,7):
    print("invalid choice")
    sys.exit()

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

if choice == 1:
    res=num1 + num2
elif choice == 2:
    res=num2 - num1
elif choice == 3:
    res=num1 * num2    
elif choice == 4:
    res=num1 / num2 
elif choice == 5:
    res=num1 % num2    
elif choice == 6:
    res=num1 ** num2    
elif choice == 7:
    res=num1 // num2  
    
print("Result is:",res)