# fault code
""" 
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)

print_range(1, 5)
"""


# code corrected
def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n=n+1
        # break
    
print_range(1, 5)