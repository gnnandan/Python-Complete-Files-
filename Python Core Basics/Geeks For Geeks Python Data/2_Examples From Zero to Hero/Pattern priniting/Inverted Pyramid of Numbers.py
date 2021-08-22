rows=int(input("Enter the number of rows needed:"))
b=0
for i in range(rows,0,-1): # Note -1 is for inverted rows
    b=b+1 # increment b 
    for j in range(1,i+1):
        print(b,end=' ')
    print()