def count_char(s):
    count = {}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return(count)

count=input("Enter the Sentance:")
print(count_char(count))