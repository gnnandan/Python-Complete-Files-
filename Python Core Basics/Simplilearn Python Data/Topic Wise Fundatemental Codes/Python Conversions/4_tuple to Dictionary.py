data=(("Name","Nandan"),("age",23),("email","gnnandan7@gmail.com"))
print(f"before conversion {type(data)} and {data}")

data=dict(data)
print(f"after conversion {type(data)} and {data}")