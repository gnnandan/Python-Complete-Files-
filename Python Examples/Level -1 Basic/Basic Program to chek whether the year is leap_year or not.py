year=int(input("Enter the year:"))

if (year % 4 == 0) or (year % 100 != 0) and (year % 400 ==0 ):
    print("{} year is leap year".format(year))
else:
    print("{} year is not a leap year".format(year))