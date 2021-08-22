def largest(a,b,c):
    if a >= b and a >= c:
        print("{} is greater than {} and {}".format(a,b,c),",so largest num is:",a)
    elif a <= b and b >= c:
        print("{} is greater than {} and {}".format(b,a,c),",so largest num is:",b)
    else:
        a <= b and b <= c
        print("{} is greater than {} and {}".format(c,b,a),",so largest num is:",c)

def equals(largest,a,b,c):
    if a == b and a == c:
        print("a,b,c is equal,so {}={}={}".format(a,b,c))
    elif a != b and b == c:
        print("b,c is equal,so {}!={}={}".format(a,b,c))
    elif a == c and b != c:
        print("a,c is equal,so {}={}!={}".format(a,c,b))
    else:
        print("a,b,c not equal,so {}!={}!={}".format(a,b,c))

def lib(a,b,c):
    print("we can also use 'Max' library function",max(a,b,c))
        
a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))
largest(a,b,c)
equals(largest,a,b,c)
lib(a,b,c)
