# Logic operator
def operation(a,b,c):
    if a < b and b < c:
        return print("{} and {} is lessthan {} and the output of And_Gate is **{}**".format(a,b,c,a < b and b < c))
    elif a < b or b > c:
        return print("{} is lessthan {} but false in {} so output of 'Or_Gate' is **{}**".format(a,b,c,a < b or b > c))
    elif not a > b:
        return print("{} is greaterthan {} and {} the output of 'not_Gate' is **{}**".format(a,b,c,not a > b))

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
operation(a,b,c)

