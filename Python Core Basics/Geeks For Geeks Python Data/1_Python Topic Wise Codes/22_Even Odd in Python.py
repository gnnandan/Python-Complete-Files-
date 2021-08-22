"""
# QUESTION
Find the winner ?

# Algorithm
- Take input for number of coins
- take a input 1
- take a input 2
- check for even or odd
    - if even is oponent is win
    - else you win
"""

# CODE

coins=int(input("Enter the number of coins:"))
i=int(input("Enter the your choice:"))
you=int(input("Enter the opponent choice:"))

if coins % 2 == 0:
    print("last drawed coin by 'Your Opponent' so 'Opponent' win")
else:
    print("last drawed coin by 'You' so 'You' win")   
    