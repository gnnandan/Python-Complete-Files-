"""
[Note]
To print Triange use range(n) first in for loop range(i+1) in next for loop
To print Inverted Triange use range(n) first in for loop range(n-i) in next for loop

"""
s=str(input("Enter the symbol:"))
n=int(input("Enter num to display::"))

for i in range(n):# note
    for j in range(n-i):# note
        print(s,end=' ') # to print symbol in triange pattern
        # print(j,end=' ') to print number in triange pattern
    print()