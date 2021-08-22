x=int(input("Enter the number x:"))
y=int(input("Enter the number y:"))
print("-----------------------------------------------")
print("Bitwise and '&' of {} and {} is:".format(x,y),x & y)
print('\n')
# only True or 1 in this case,
"""
[True Case only in this case]
# Bitwise and '&' of 1 and 1 is: 1
"""

print("-----------------------------------------------")
print("Bitwise or '|' of {} and {} is:".format(x,y),x | y)
print('\n')
# only True or 1 in this case,
"""
[True Case only in this case]
# Bitwise or '|' of 1 and 1 is: 1
# Bitwise or '|' of 0 and 1 is: 1
# Bitwise or '|' of 1 and 0 is: 1

"""

print("-----------------------------------------------")
print("Bitwise xor '^' of {} and {} is:".format(x,y),x ^ y)
print('\n')
"""
[True Case only in this case]
# Bitwise xor '^' of 0 and 1 is: 1
# Bitwise xor '^' of 1 and 0 is: 1
"""

print("-----------------------------------------------")
print("Bitwise leftshift '<<' of {} and:".format(x),x << 2)
print('\n')
"""
[leftshift - multiples with power of 2, (**2)]
# Bitwise leftshift '<<' of 2 and 2 ** 2 is: 8
# Bitwise leftshift '<<' of 3 and 2 ** 2 is: 12
# try adding x << 3
# Bitwise leftshift '<<' of 6 and 2 ** 2 ** 2 is: 48
"""

print("-----------------------------------------------")
print("Bitwise rightshift '>>' of {}:".format(x),x >> 2)
print('\n')
"""
[rightshift- divides with power of 2, (**2) ]
# Bitwise rightshift '>>' of 3: 0
# try with x>>3
# Bitwise rightshift '>>' of 2: 0
"""

print("-----------------------------------------------")
print("Bitwise negation '~' of {}:".format(x),~x)
print('\n')
"""
[negation]
# Bitwise negation '~' of 6: -7
"""

