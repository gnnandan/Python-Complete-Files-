def getFirst_Digit(num):
    while num >=10:
        num=num//10
    return num

num=int(input("Enter the numbers:"))
print(f"The first digit is {getFirst_Digit(num)}")