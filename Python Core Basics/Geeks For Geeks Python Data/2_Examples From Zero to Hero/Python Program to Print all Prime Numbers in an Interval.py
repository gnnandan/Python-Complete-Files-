lower=int(input("Enter starting range:"))
upper=int(input("Enter ending range:"))
print("Prime numbers from {} to {} are:".format(lower,upper))

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) ==0:
                break
        else:
            print('{}'.format(num),end=' ')