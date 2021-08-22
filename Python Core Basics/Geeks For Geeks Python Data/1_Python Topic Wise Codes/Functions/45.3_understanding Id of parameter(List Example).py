def fun(l):
    print(f"The initial id of *{id(l)}*")
    l.append("Data appended")
    print(f"The id of l after appending *{id(l)}* and l is {l}")
    
l=[1,2,3,4,5]
print(f"The id of l before appending *{id(l)}* and l is {l}")
fun(l)
