"""
# Membership Test Operators in Python {GeeksforGeeks}
[check by changing in if statements]
Check with some different values
"""

string="Hello This is Nandan"
Dictionary={1:"Nandan",2:"Pavan"}
list=['a','b','c','d','e']
tuple=(1,2,3,4,5,6)
set={100,200,300,400,500}

if "Hello" in string:
    print("Checked for 'sub-string' in string **{}**".format("Hello" in string))
elif "Hello" not in string:
    print("Checked for 'sub-string' not in string **{}**".format("Hello" not in string))
    
if 1 in Dictionary:
    print("Checked for 'key' in Dictionary **{}**".format(1 in Dictionary))
    
elif 1 not in Dictionary:
    print("Checked for 'key' not in Dictionary **{}**".format(1 not in Dictionary))
    
if 'a' in list and 1 in tuple and 100 in set:
    print("Checked for 'member' in list **{}**".format('a' in list))
    print("Checked for 'member' in tuple **{}**".format(1 in tuple))
    print("Checked for 'member' in set **{}**".format(100 in set))
elif'a' in list and 1 in tuple and 100 in set:
    print("Checked for 'member' not in list **{}**".format('a' not in list))
    print("Checked for 'member' not in tuple **{}**".format(1 not in tuple))
    print("Checked for 'member' not in set **{}**".format(100 not in set))

else:
    print("invalid")
    