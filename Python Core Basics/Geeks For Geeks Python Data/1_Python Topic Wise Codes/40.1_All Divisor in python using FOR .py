# Task we need to print all the divisors of the given number
n=int(input("Enter number:"))
for x in range(1,n+1):
    if (n % x == 0):
        print(x)
    else:
        continue
        n+=1