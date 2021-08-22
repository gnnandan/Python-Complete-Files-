row=int(input("Enter the number:"))
for row in range(1,row+1):
    for column in range(1,row+1):
        print("*",end=' ')
    print() 
for row in range(row,0,-1):
    for column in range(row):
        print("*",end=' ')
    print()