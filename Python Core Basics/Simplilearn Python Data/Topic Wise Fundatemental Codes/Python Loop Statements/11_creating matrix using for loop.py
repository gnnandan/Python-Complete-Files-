row = int(input("Enter number of rows:"))
column = int(input("Enter number of column:"))

matrix = []
val = []
for i in range(0,row):
    for j in range(0,column):
        val.insert(j,input(f"Enter the {i} and {j} Elements"))
    matrix.insert(i,val)
    val = []
print(matrix)