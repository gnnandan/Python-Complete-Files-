def DefaultArgument(id,name,age):
    print(f"my id {id}")
    print(f"my name {name}")
    print(f"my age {age}")

# Note using Keyword argument will be more benefits 
print("Keyword argument")
DefaultArgument(id=1,name="Nandan",age=21) #Note if you used argument=value it will be keyword argumnet

print()
DefaultArgument(id=2,name="Yashas",age=21)
