row=int(input("Enter the number:"))
for row in range(1,row+1):
    for column in range(1,row+1):
        print(column,end=' ')
    print()