"""
[summary]
while loop
"""
i=0
n=int(input("Enter how many times you need to repeat:"))
inputs=input("Enter what you need to repeat:")
while i < n:    
    print(inputs)
    i=i+1 # Note : if you not initialized it it will repeat infinately 
    # break