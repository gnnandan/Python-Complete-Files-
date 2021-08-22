num=int(input("Enter the number:"))

if num < 0:
    print("Please enter a valid number:")
else:
    sum=0
    while num > 0:
        sum=num*(num+1)/2   
        print("The sum of {} is:".format(num),sum)