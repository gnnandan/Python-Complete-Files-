# nested if statement
def nested_if(a):
    if a > 0:
        if a >= 20:
            return(f"{a} is greter then 20")
        return ("condition 2 ends")
    return ("condition 1 ends")

a=int(input("Enter a: >> "))
print(nested_if(a))