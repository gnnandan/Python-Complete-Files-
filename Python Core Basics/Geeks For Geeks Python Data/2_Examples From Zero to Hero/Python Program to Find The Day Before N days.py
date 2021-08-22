"""
[formula]
(d-n)%7
"""

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] #taken dictionary for easy operation
def day_before(n,d):
    
    #Note
    day=(d-n)%7
    if day == 1:
        print("The day is:",days[1])
    elif day == 2:
        print("The day is:",days[2])
    elif day == 3:
        print("The day is:",days[3])
    elif day == 4:
        print("The day is:",days[4])
    elif day == 5:
        print("The day is:",days[5])
    elif day == 6:
        print("The day is:",days[6])
    elif day == 7:
        print("The day is:",days[7])
    else:
        print("Its present day")



n=int(input("Enter the present day id by seeing it in days:"))
d=int(input("Enter the how many day before the present you need:"))
day_before(n,d)