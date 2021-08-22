# ax2 + bx + c
def eq(a,b,c):
    d=(b**2)-(4*a*c)
    eq1=-b+(d)/2*a
    eq2=-b-(d)/2*a
    print("The equaltion is {} and {}".format(eq1,eq2))
    
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
eq(a,b,c)