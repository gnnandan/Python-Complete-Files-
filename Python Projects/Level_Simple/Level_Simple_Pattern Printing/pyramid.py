def pyramid():
    row=int(input("Enter the number:"))
    
    # Note actual logic
    for i in range(0,row): # this for loop for space(outer for loop)
        for j in range(0,row-i-1): # if row=4, i=0 4-0-1=3(spaces)
            print(end=" ")
        for j in range(0,i+1): # star pattern starts from 0th row and keeps increasing till given row
            print("*",end=" ")
        print()
    
print(pyramid())