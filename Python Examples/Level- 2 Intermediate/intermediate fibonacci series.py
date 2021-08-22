n=int(input("Enter the value:"))
a=0
b=1
sum=0
count=1
print("Factorial series are:")
while count<=n:
    print(sum,end=" ")
    # logic
    count=count+1
    a=b
    b=sum
    sum=a+b
