num=int(input("Enter the number:"))
factorial=1

if num < 1:
    print("Not exist!")
elif num == 0:
    print("Factorial of {} is 1".format(num))
else:
    # logic
    for i in range(1,num+1):
        factorial=factorial * i
    print("The factorial of",num,"is",factorial)