"""
Fill in the blanks to make the
is_power_of function return whether the number is a power of the given base. 
Note: base is assumed to be a positive number. 
Tip: for functions that return a boolean value, 
you can return the result of a comparison.
"""
def is_power_of(number,base):
    if number < base:
        return number == 1
    
    # recursive function
    result=number//base
    return is_power_of(result,base)

number=int(input("Enter the number:"))
base=int(input("Enter the base number:"))
print(f"The number {number} with its base {base} is {is_power_of(number,base)}")