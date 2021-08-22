database={"username": "Nandan","password": 1234567}
username=input("Enter username >>")

while username != database.get("username"):
    print("Enter the correct username ❌ ")
    break
else:
    print(f"{username} your username is verified...! ✅ ")
    print(f"please enter the password....! ⏭ ")
    password=int(input("Enter password >>"))
    while password != database.get("password"):
        print("Enter the valid password... ❌ ")
        break
    else:
        print("Your password is varified...! ✅ ")
