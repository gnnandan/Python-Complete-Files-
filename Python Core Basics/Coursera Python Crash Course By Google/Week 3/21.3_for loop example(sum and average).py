numbers=[10,20,30,40,50,60,70,80,90,100]
sum=0
length=0

for value in numbers:
    sum=sum + value
    length=length+1
print(f"Total sum is {str(sum)} and average length is {str(sum/length)}")