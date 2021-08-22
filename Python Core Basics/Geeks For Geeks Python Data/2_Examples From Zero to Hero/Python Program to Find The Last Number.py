"""
[summary]
to find last no in positive side use n%10
to find last no in negative side use abs(n)%10
"""
n=int(input("Enter the numbers:"))

if n > 0:
    ld = n % 10
    print("The last number  in +ve side is:",ld)
else:
    n < 0
    ld = abs(n) % 10
    print("We use abs to convert -ve no to +ve no")
    print("The last number in -ve side is:",ld)