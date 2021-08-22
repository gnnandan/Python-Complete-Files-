"""
Algorithm
# using for 
- take n multiple
    - create a function that takes n as parameter 
    - create a for loop with range 1 to 11
    - print the operation using **
    - increment by one using i=i+1
- call functions with parameter

# using while
- take n multiple
    - initialize i=0
    - create a function that takes n as parameter 
    - create a while loop with i<=10
    - print the operation using **
- call function with parameter
    """

n=int(input("Enter number that you multiples:"))

def usg_for(n):
    print('Multiplication table using "for loop"')
    for i in range(1,11):
        print(n,'*',i,'=',n*i)# **
        i=i+1 # i+=1 it is also ok
        
def usg_while(n):
    print('Multiplication table using "while loop"')
    i=0
    while i<=10:
        print(n,'*',i,'=',n*i)# **
        i+=1
    
usg_for(n)
usg_while(n)