x=int(input("Enter the number:"))
if x>0:
    ld=x%10
    print("The last digit of 'positive numbers' {} is:".format(x),ld)
elif x<0:
    ld=abs(x)%10
    print("The last digit of 'negative numbers' {} is:".format(x),ld)
else:
    print("Invalid")
"""
[summary]
abs(x) converts x from negative numbers to positive number
and prints the last number
"""