# n=int(input("Enter num to display::"))
n=5


"""
[Algorithm]
/* for i in range(n): - it will collects the numbre of iterations to print 
    for j in range(n-i+1): - it will print the white spaces from left
    for k in range(2*i+1): - it will print the pattern for given range
"""
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(2*i-1):
        print("*",end=' ')
    print()