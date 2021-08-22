# Note Keyword-variable length arguments are bassically dictionary
def KVLA(id,**data):
    print(f"DEtails of id is mandatory {id}") # Note if you didn't used id to display it won't display
    for k,v in data.items(): #Note k-key v-value
        print(f"{k} is {v}")

print("Keyword-variable length arguments")
print(KVLA(id=1,name="Nandan",lucy_no=7))
# print()
# print(KVLA(id=2,name="Yashas",lucy_no=8))
