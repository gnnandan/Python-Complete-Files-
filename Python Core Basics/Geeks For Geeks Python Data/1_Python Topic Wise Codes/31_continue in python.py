"""
[summary]
printing the numbers which is not divisible from n

"""

n=[10,16,17,18,19,20]
print("Display number which is not divisible by 5 from list")
for x in n:
    if x % 5 == 0:
        continue
    print(x)
    