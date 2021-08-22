import math
def getFirst_Digit(num):
    d=int(math.log10(num))
    res=num//(10**d)
    return res

num=int(input("Enter number:"))
print("The first digit is:",getFirst_Digit(num))