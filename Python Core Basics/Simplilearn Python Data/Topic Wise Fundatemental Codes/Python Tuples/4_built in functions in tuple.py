x=("Bangalore","Mysore","Tiptur","Tumkur","Bangalore")

# tuple.count() --->counting the number of occurance of particular elements
count=x.count("Bangalore")
print(f"The number of time occurred is '{count}'")

# sum()--->to calculate the total
data=(10,20,30,40,50,60,70,80,90,100)
print(f"Total sum of a tuple is '{sum(data)}'")

# len()--->to calculate the length of the tuple
print(f"The length of a tuple is '{len(data)}'")

# sum()/len() can be used to find the average of tuple values
print(f"The sum of tuple is '{sum(data)}' and len of tuple is '{len(data)}' so the average of tuple is '{sum(data)/len(data)}'")

# max() to find the maximum number in a tuple(iterable)
print(f"The maximum number in a tuple is '{max(data)}'")

# min() to find the minimum number in a tuple(iterable)
print(f"The minimum number in a tuple is '{min(data)}'")