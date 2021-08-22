def nxt_prime(n):
    if n <=1:
        return print(False)
    else:
        for i in range(2,n):
            if n % i == 0:
                return print(False)
            return print(n+i)

n=int(input("Enter the present prime number:"))
nxt_prime(n)