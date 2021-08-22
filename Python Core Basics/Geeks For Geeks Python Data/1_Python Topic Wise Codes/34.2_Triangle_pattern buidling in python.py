s=str(input("Enter the symbol:"))
n=int(input("Enter num to display::"))

for i in range(n):# note
    for j in range(i+1):# note
        print(s,end=' ') # to print symbol in triange pattern
        # print(j,end=' ') to print number in triange pattern
    print()