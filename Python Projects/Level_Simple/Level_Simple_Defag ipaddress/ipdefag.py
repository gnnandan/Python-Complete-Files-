import socket

def ipaddress(address):
    new_address=""
    split_address=address.split(".")
    seperate="[.]"
    new_address=seperate.join(split_address)
    return new_address

hostname=socket.gethostname()
address=socket.gethostbyname(hostname)
print(f"hostname:{hostname}")
print(f"actual ipaddress {address}")
print(f"ipaddress after defag:{ipaddress(address)}")