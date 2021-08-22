# id()
a="Nandan G N"
b=10
print("Unique identifier of {} and {}\n".format(a,b),"a:",id(a),"b:",id(b))

c="a"
d="a"
print("Unique identifier of {} and {}\n".format(c,d),"c:",id(c),"d:",id(d))

print("\n")
# is()
a=10
b=10
c=100
print("check 'a' is similar to 'b':",a is b,"\ncheck 'c' is similar to 'a':",c is a)