data=[("Name","Nandan"),("Age",23),("Branch","CSE")]
print(f"Before conversion {type(data)},'{data}")
New_data=dict(data)
print(f"After conversion {type(New_data)},'{New_data}'")