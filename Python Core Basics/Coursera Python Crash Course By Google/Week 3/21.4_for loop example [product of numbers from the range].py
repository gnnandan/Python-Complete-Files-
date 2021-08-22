
def logic(j):
    product=1.
    for n in range(1,j):
        product= product * n
    print(f"The product of {j} numbers is {product}")

j=int(input("Enter the number:"))
logic(j)
