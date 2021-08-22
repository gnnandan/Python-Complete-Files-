import sys


data=(
1,
1.1,
'1',
True,
0+1j,
[1,2,3,4,5,6],
('a','b','c'),
{1:'one',2:'two'},
{1,2,3,'one','two','three'}
)

for chk in data:
    print("The type of {}:".format(chk),type(chk))
    
def chk_fuc():
    return None

chk_fuc()

class chk_cls():
    def chk_fuc(self):
        return None
        
obj=chk_cls()
print("The type is class:",type(obj))
print("The type is function:",type(chk_fuc))