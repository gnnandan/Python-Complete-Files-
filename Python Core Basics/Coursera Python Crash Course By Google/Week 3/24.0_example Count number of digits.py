'''
Complete the function digits(n) that returns how many digits the number has. 
For example: 25 has 2 digits and 144 has 3 digits. 
Tip: 
you can figure out the digits of a number by dividing it by 10 
once per digit until there are no digits left.
'''

def count_digit(n):
    count=0
    if n ==0 :
        return 1
    else:
        while n > 0:
            count+=1
            n=n//10
        return count
n=int(input("Enter the number to find how many digits are there:"))    
print(f"The total number of digits in {n} is: {count_digit(n)}")