def fib(n):
    n=n-1
    if n==0 and n==1:
        return print(1)
    a=b=1
    c=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    print(c)

n=int(input("Enter number:"))
fib(n)