# checking odd or even 
def chk_parity(n):
        if n % 2==0:
            return print("{}".format(n % 2),True)
        return print("{}".format(n % 2),False)
    
n=int(input("Enter n:"))
chk_parity(n)