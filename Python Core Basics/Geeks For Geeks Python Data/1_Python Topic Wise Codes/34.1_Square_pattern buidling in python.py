"""
Algorithm
- take input symbol
- take input how many time the symbol needs to be repeated
    - construct nested for loop to print pattern
    - print() - to have new lines
"""
s=str(input("Enter the symbol:"))
n=int(input("Enter num to display::"))
for i in range(n):
    for j in range(n):
        print(s,end=' ')
    print()