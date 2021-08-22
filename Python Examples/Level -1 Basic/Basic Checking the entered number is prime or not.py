num=int(input("Enter the number:"))
flag=False
if num > 1:
    for i in range(2,num):
        if (num % i == 0):
            flag=True
        break
if flag:
    print("{} number is not a prime number".format(num))
else:
    print("{} number is prime number".format(num))