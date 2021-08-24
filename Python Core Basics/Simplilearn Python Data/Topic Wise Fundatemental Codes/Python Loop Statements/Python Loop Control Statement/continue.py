x = "First Sentence. Second Sentence"
# ! continue (skipps) the perticular string of function 
for i in x:
    if i == '.':
        continue
    print(i, end="")