# counting the ways to reach nth stair [Example]
# Note 1 1 2(1+1) 3(2+1) 5(2+3)====>1 1 2 3 5 8......
"""
[Algorithm]
- check if the present state is 0 or 1, if then print 1
-else
    - print(1,1,end=' ') the initial state
    - initially a=1,b=1
    - loop from 2 to n+1 
        - c=a+b
        - print(c,end=' ')
        - a=b
        - b=c

    """

n=int(input("Enter the nth number:"))

if n==0 and n==1:
    print(1)
else:
    print(1,1,end=' ')
    a=b=1
    for c in range(2,n+1):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
    
