# printing 1 to 100 
# n=int(input("Enter the n:"))
# i=0
# while i < n:
#     for i in range(1,n*10+1,1):
#         print(i,end=' ')
#     print()
#     i+=1
    
# multiple of numbers from 1 to 100
for i in range(1,11):
    for j in range(i,i*10+1,i):
        print(j,end=' ')
    print()
    
# nested loop in list of lists
print("\n")
print("Nested for loop can be used to traverse list of lists")
ll=[[10,20,30,40],[10,20,30],[10,20],[10]]

for l in ll:
    for x in l:
        print(x,end=' ')
    print()