def square(n):
    return n*n

def sum_square(x):
    sum=0
    for n in range(0,x):
        sum +=square(n)       
    print(f"The sum of square is: {sum}")

x=int(input("Enter the number to find sum of square:"))
print(sum_square(x))