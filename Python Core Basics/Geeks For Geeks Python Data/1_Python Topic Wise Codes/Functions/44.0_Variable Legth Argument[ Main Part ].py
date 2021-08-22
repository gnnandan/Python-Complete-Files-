# Note variable length argumets take any number of values
# Note * indicates the variable length argument and it is consider as tuple elements
def VLA(*element):
    res=0
    for x in element:
        res= res + x
    return res

print(VLA(10,20,30))
print()
print(VLA(10,20))
print()
print(VLA(10))
print()
print(VLA())