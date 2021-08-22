def fun(l):
    l.append("New Data")
    print(f"After appending new data to list **{l}**")
    
l=[1,2,3,4,5]
print(f"Before append the New Data to list **{l}**")
fun(l)
