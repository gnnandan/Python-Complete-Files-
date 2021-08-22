s="Hi this is Nandan G N"

# making the string upper case
print("Upper:",s.upper())

# making the string lower case
print("Lower:",s.lower())

# finding the index of perticular character
print("index:",s.find("is"))
print("index:",s.index("is"))

# spliting the string
print("Split:",s.split("is"))

# replacing certain part of string
print("Replace:",s.replace("Nandan G N","NANDAN G N"))

# rpartition 
print("rpartition:",s.rpartition("is"))

# concatenation
a="Hello,"
b="Coders"
c=a+" "+b #adding both string
print("concatenation:",c)
print("concatenation:",a+" "+b)

# concatenation of more string
a="Hello"
b="Coders"
c="Nandan"
d="Here"
# {} are called as placeholders
print("Use format:",f"{a},{b} {c} {d}!.")