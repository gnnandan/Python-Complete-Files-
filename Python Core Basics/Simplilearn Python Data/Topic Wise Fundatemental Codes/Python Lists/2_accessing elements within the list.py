#list of combinations of all
x=[1,2,'a','b','aa1','bb2']
print(f"List of combinations: {x} and {type(x)}")
print()
print("accessing the elements of list")
print()
print("accessing single element")
print(f"Positive index '{x[0]}' || Negative index of '{x[-1]}'")
print(f"Positive index '{x[1]}' || Negative index of '{x[-2]}'")
print(f"Positive index '{x[2]}' || Negative index of '{x[-3]}'")

print()
print("accessing the range of elements")
print(f"all element accessing '{x[:]}'")
print(f"Positive index '{x[0:2]}' || Negative index of '{x[-2:-1]}'")
print(f"Positive index '{x[0:3]}' || Negative index of '{x[-3:-1]}'")
print(f"Positive index '{x[0:4]}' || Negative index of '{x[-4:-1]}'")

print()
print("accessing the range of elements from certain position")
print(f"Positive index '{x[:3]}' || Negative index of '{x[:-1]}'")
print(f"Positive index '{x[2:]}' || Negative index of '{x[-3:]}'")
print(f"Positive index '{x[3:5]}' || Negative index of '{x[-4:-2]}'")

print()
# important
print("reversing the list")
print(f"reversed x is {x[::-1]}")