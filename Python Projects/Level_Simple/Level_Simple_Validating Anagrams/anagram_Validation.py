"""
Note
An anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once    
"""

def anagrams(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    return sorted(word1) == sorted(word2)

print(anagrams("cinema","iceman"))
print(anagrams("Nandan","dannan"))
print(anagrams("man","mans"))