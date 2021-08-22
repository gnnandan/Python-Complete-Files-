num=int(input("Enter the number to check:"))

order=len(str(num))
sum=0
temp=num
while temp > 0:
    digit=temp % 10
    sum=sum+digit ** order
    temp=temp//10

if num == sum:
    print("{} The number is armstrong".format(num))
else:
    print("{} The number is not a armstrong".format(num))