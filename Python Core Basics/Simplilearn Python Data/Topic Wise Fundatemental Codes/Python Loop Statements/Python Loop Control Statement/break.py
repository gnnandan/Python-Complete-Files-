x = "First Sentence. Second Sentence"
# ! breakig when '.' comes
for i in x:
    if i == '.':
        break
    print(i, end="")
    
    