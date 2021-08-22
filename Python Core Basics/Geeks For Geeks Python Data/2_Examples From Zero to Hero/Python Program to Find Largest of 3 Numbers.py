a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))


if a > b and a > c:
    print("{} is greater than {} and {}".format(a,b,c))
elif b > a and b > c:
    print("{} is greater than {} and {}".format(b,a,c))
elif c > a and c > b:
    print("{} is greater than {} and {}".format(c,a,b))
else:
    print("{} or {} or {} are equal".format(a,b,c))
