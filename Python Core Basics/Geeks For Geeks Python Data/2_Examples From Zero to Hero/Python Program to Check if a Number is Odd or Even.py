def chk(num):
    if num % 2==0:
        print("The number {} is even".format(num))
    else:
        print("The number {} is odd".format(num))
        
a=float(input("Enter num:"))
chk(a)