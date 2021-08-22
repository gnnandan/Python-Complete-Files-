# Factorial
def factorial(n):
    print(f"Factorial called with {n}")
    if n < 2:
        print("Returning: 1")
        return 1
    result =n * factorial(n - 1)#this is returcive procedure
    print(f'Returning: {result}')
    return result  

factorial(10)