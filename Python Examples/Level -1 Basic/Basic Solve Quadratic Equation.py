def eq(a,b,c):
    d=(b**2)-(4*a*c)
    solve_positive=(-b +(d)** 0.5) / 2 * a
    solver_negative=(-b -(d)** 0.5) / 2 * a
    print(solve_positive,solver_negative)
    
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
eq(a,b,c)