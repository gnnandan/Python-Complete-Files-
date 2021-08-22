n=int(input("Enter number:"))
x=1
while x <= n:
    if(n % x == 0):
        print(x)
    x+=1