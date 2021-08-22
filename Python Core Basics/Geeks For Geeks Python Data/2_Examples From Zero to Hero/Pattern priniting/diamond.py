# n=int(input("Enter the number:"))
n=5
row=5

def upper_triangle():
    k=2 * row-2 # used to print spaces 
    for i in range(row): #outer loop for upward triangle
        for j in range(k): #inner loop to print spaces in upward triangle
            print(end=" ")
        k=k-1 # decrement spaces for each iteration
        for j in range(i+1): #inner loop to print stars in upward triangle
            print("*", end=' ')
        print()
        
def lower_triangle():
    k=row-2 # used to print spaces 
    for i in range(row,-1,-1): #outer loop for downward triangle
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1 # increment spaces for each iteration
        for j in range(0,i+1):#inner loop to print stars in downward triangle
            print("*",end=" ")
        print()

upper_triangle()
lower_triangle()
    
    