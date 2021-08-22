num=int(input("Enter the number of digits:"))
i=0
while num > 0:
    num=num//10
    i=i+1
print("Total number of digit is {}".format(i))