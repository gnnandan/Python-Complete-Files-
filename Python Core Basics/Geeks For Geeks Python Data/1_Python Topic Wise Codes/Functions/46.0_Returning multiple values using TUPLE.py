def rtn_mv(x,y):
    floor_division=x//y
    power=x**y
    return (floor_division,power) #Note(You can add n numbers also)it considerd as tuple and it returns as a tuple
"""
[try with other returning values]
return [floor_division,power]
or
return {} 
"""

f,p=rtn_mv(10,20)
print(f"floor_division value is {f}")
print(f"power value is {p}")