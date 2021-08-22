# String in python are immutable 
name="Python"
print(len(name))

# indexing
print("indexing")
print("0:",name[0])
print("1:",name[1])
print("-1:",name[-1])

print()

# Slicing
print("Slicing")
print("0:1 >>",name[0:1])
print("0:3 >>",name[0:3])
print("1: >>",name[1:])
print(":-1 >>",name[:-1])
print("::1 >>",name[::1])
print("::-1 >>",name[::-1])

# modifying 
print("Modifying a string")
s ="A knog string with a silly typo"
m_s=s.replace("knog","long")
print(f"String after modifying '{m_s}'")

print()

# choosing the index
pets="Cats & Dogs"
print(pets.index("&"))
m_pets=pets.replace("&", "and")
print(m_pets)

print()

# using 'in' to choose the if substring present or not
print("Dragon" in pets)
print("Dogs" in pets)
print()

# uppercase
print(m_s.upper())
print(m_s.lower())
print()

# striping the not needed things
st="    stripped not needed        "
print(f"just left_strip: {st.lstrip()}")
print(f"just right_strip: {st.rstrip()}")
print(st.strip())
print()

# counting the number of occurance of characters
m_s ="A long string with a silly typo"
print(f"count: {m_s.count('s')}")
print()


# startswith() and endswith() and numeric()
m_s ="A long string with a silly typo"
print(f"startswith: {m_s.startswith('A')}")
print(f"endswith: {m_s.endswith('po')}")
print(f"isnumeric: {m_s.isnumeric()}")
print()

# join() for con catenation
s1=" "
s2=["This","is","a","phrase","joined","by","spaces"]
# " ".join(["This","is","a","phrase","joined","by","spaces"])
print(f"joining s1 and s2:",s1.join(s2))
print("...".join(["This","is","a","phrase","joined","by","dots"]))
print()

# split()

print("We can split the strings using .split()".split())