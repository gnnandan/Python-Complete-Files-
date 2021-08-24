from typing import Counter


string = input("Enter input string: ")
no = int(input("Enter input number: "))
Counter = 0
while Counter <= no:
    print(f"{Counter} is {string}")
    Counter+=1