# arithmetic operator
def operation(a,b):
    operator=input("Enter the operator:")
    if operator == '+':
        return print("sum of {} and {} is:".format(a,b),a+b)
    elif operator == '-':
        return print("diff of {} and {} is:".format(a,b),b-a)
    elif operator == '*':
        return print("product of {} and {} is:".format(a,b),a*b)
    elif operator == '/':
        return print("{} by {} is:".format(a,b),a/b)
    elif operator == '%':
        return print("modulus of {} and {} is:".format(a,b),a%b)
    elif operator == '//':
        return print("floor of {} and {} is:".format(a,b),a//b)
    elif operator == '**':
        return print("{} power of {} is:".format(a,b),a**b)
    else:
        print("Invalid operator")

a=int(input("Enter a:"))
b=int(input("Enter b:"))
operation(a,b)

