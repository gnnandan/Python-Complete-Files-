
"""
[code is wrong]
def count_down(start_number):
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)
"""
# We need to fix it 
# code to fix

# Remember: whenever you're writing a loop check that you're initializing all the variables you want to use before you use them
def count_down(start_number):
    while(start_number > 0):
        print(start_number)
        start_number -= 1
    print("Zero!")
count_down(3)