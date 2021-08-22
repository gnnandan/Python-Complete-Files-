from typing import Counter


a=int(input("Enter starting year: "))
b=int(input("Enter ending year: "))
def year():
    for year in range(a,b):
        if year % 4 ==0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("Entered year {} is leap year".format(year))
                else:
                    print("Entered year {} is not a leap year".format(year))
            else:
                print("Entered year {} is a leap year".format(year))
        else:
            print("Entered year {} is not a leap year".format(year))
            
        
year()