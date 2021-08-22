# Note here id is a parameter before variable length arguments
def VLA(id,*element):
    print("Enter Details of id:",id)
    res=id
    for x in element:
        res= res + x
    return res

print(VLA(1,10,20,30))
print()
print(VLA(5,10,20))
print()
print(VLA(4,10))
print()
print(VLA(12))