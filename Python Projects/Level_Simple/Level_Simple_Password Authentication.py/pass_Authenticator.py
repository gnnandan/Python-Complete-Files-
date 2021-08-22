import getpass

database={"Nandan":"1234567","Yashas":"12345678"} #sample database

username=input("Enter the username >> ")
password=getpass.getpass("Enter the password >> ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password=getpass.getpass("Try again...")
        break
print(f"{username} password varified successfully")