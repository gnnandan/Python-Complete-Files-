n = int(input("Enter the num of sum you want: "))
i = 0
sum = 0
while i <= n:
    if i % 2 == 0:
        sum = sum +i
    i+=1
print(f"The sum of {n} even number is :{sum}")