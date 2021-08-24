n = int(input("Enter the number of pattern n:"))
for i in range(1,n+1): # ! for columns
    for j in range(1,i+1): # ! for rows
        print(j, end="")
    print()