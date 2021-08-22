val=int(input("Enter the multiple of 7:"))
while val % 7 != 0:
    val=int(input("Enter the multiple of 7:"))
else:
    print(f"{val} is a multiple of 7")
    