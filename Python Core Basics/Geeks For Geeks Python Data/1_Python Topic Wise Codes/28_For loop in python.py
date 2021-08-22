# Note: for in  str
str="Be always down to earth"
for s in str:
    print(s)

print('\n')

# Note: for in list
quality =['Good','Positive','Humanity','Truth','Courage']
print('Qualities of Human Being')
for quality in quality:
    print(quality)
print('\n')
    
# Note: for and range list
for x in range(0,10):
    print(x)

# Note: divisible of numbers
n=int(input("Enter the number to get its divisible:"))
for x in range(0,100):
    if x % n ==0:
        print(x)
print('\n')          
# Note: For ,List index 
quality =['Good','Positive','Humanity','Truth','Courage']
for i in range(len(quality)):
    print(quality[i])

print('\n')
    
# Note this and above that are similar
for i in quality:
    print(i)
    
print('\n')

# Note for with element and index
quality =['Good','Positive','Humanity','Truth','Courage']
for i in range(len(quality)):
    print("index:",i,"Values:",quality[i])