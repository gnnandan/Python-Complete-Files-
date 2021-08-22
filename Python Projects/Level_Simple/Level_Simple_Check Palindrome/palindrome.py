def palindrome(sentance):
    for i in (".,?/><={}[]()*&%$#@%*:|\/!"):
        sentance=sentance.replace(i,"")
        
    else:
        # create empty list
        palindrome=[]
        
        # split the input sentance
        words=sentance.split(' ')
        
        # compare word by word using for loop
        for word in words:
            word=word.lower()
            
            # logic
            if word == word[::-1]:
                print(f"{word} is palindrome")
                palindrome.append(word)
            else:
                print(f"{word} is not palindrome")
                palindrome.append(word)
        return palindrome
    
sentance=input("Enter the sentance:")
print(palindrome(sentance))
            