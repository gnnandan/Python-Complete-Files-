
"""
Note 
You can also specify text alignment using the greater than operator: >. 
For example, the expression {:>3.2f} would align the text three spaces to the right, 
as well as specify a float number with two decimal places

"""

price=100
tax=0.18
total_price=price+price * tax

# formatting methods
# Note Method 1
print(f"Formatting the String 'METHOD 1' >> The total price of a goods is {total_price}")
# Note Method 2
print("Formatting the String 'METHOD 2' >> The total price of a goods is {total_price}".format(total_price=total_price))

#Note Method 3
print("Formatting the String 'METHOD 3' >> The total price of a goods is {}".format(total_price))

print()

# formatting the string to the specific decimal point
# Note formatting to specific decimal point Method 1
print(f"Formatting to specified decimal point 'METHOD 1'>> The total price of a goods is {total_price:.2f}")
# Note formatting to specific decimal point Method 2
print("Formatting to specified decimal point 'METHOD 2'>> The total price of a goods is {:.2f}".format(total_price))

