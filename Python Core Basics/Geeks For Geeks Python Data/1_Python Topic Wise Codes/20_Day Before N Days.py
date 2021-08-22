"""
[Table]
d|Days
------
0|Sunday
1|Monday
2|Tuesday   
3|Wednesday
4|Thursday
5|Friday
6|Saturday

[formula]
(d-n)%7
"""
# d= no of day
# n= how many days before we want to know the day
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
d=int(input("Enter the present day id by seeing it in days:"))
n=int(input("Enter the how many day before the present you need:"))
day=(d-n)%7
if day == 0:
    print("The day is:",days[0],"and d id is",day)
elif day ==1:
    print("The day is:",days[1],"and d id is",day)
elif day ==2:
    print("The day is:",days[2],"and d id is",day)
elif day ==3:
    print("The day is:",days[3],"and d id is",day)
elif day ==4:
    print("The day is:",days[4],"and d id is",day)
elif day ==5:
    print("The day is:",days[5],"and d id is",day)
else:
    print("The day is:",days[6],"and d id is",day)  