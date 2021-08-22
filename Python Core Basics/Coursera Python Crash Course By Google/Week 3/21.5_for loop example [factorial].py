def logic(n):
    factorial=1
    for n in range(1,n+1):
        factorial = factorial * n
    print(f"The factorial of n is {factorial}")
    
n=int(input("Enter the number:"))
logic(n)