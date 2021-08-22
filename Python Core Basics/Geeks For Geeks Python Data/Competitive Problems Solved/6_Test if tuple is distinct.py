    """
    Algorithm
    def a empty set() 
    start iteration using for loop to tuple
    check condition 
        if element is not there means add and print (Distinct)
        if element is there print(Not Distinct)
    """
    
def tup(a):
    s=set()
    for x in a:
        if x in s:
            return print("Not Distinct")
        s.add(x)
    return print("Distinct")
    

a=(1,2,3,4,5,6,6)
tup(a)
