start_year =int(input("Enter the input start year:"))
end_year=int(input("Enter the input end year:"))
print("The list of leap years from {} to {} is:".format(start_year,end_year))
for i in range(start_year,end_year + 1):
    if (i % 4) == 0 and (i % 100) != 0 or (i % 400) == 0: #Note important line 
        print(i)