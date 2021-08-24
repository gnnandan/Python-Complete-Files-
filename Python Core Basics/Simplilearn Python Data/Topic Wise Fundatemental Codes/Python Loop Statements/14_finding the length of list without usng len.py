x = input("Enter the list item:")
item = list(x)
i = 0
length = 0

try:
    while item[i]:
        length+=1
        i+=1
except IndexError:
    print(f"The length of list is: {length}")
    
    