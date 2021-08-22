# arithmetic operator
def operation(a,b):
    operator=input("Enter the operator:")
    if operator == '+':
        return print("sum is:",a+b)
    elif operator == '-':
        return print("diff is:",b-a)
    elif operator == '*':
        return print("product is:",a*b)
    elif operator == '/':
        return print("quotient is:",a/b)
    elif operator == '%':
        return print("reminder(modulus) is:",a%b)
    elif operator == '//':
        return print("floor division is:",a//b)
    elif operator == '**':
        return print("power is:",a**b)
    else:
        print("Invalid operator")

a=int(input("Enter a:"))
b=int(input("Enter b:"))
operation(a,b)

