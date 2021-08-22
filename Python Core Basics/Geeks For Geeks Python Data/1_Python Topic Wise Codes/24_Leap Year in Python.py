#Algorithm

"""
Steps
- take year as input 
- construct a if, elif and else statement based on requiremets
- check for condition
    - if year is multiple of 4 but not 100
    - if year is multiple of 400
        - print leap year
    - else 
        - print not a leap year
"""
# code
def Check_leap(year):
    if year % 4 == 0:
        if year % 100 == 0: 
            if year % 400 == 0:
                print("{} is a leap year".format(year))
            else:
                print("{} is not a leap year".format(year))
        else:
            print("{} is a leap year".format(year))
    else:
        print("{} is a not leap year".format(year))
        
year=int(input("Enter the year:"))        
Check_leap(year)