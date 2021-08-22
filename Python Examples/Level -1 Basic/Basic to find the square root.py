import math
def sqrt_find(num):
    print("The square root of {} is(Type 1):".format(num),num**0.5)
    print("The square root of {} is(Type 1):".format(num),math.sqrt(num))

num =int(input("Enter num:"))
sqrt_find(num)