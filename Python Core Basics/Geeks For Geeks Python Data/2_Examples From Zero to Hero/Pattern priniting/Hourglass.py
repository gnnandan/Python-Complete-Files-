s='*'
n=int(input("Enter the number:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for j in range(2*i-1):
        print(s,end=' ')
    print()
    
for x in range(n):
    for y in range(n-x-1):
        print(" ",end=' ')
    for y in range(2*x+1):
        print(s,end=' ')
    print()