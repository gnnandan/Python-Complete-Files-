import smtplib

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("gnnandan7@gmail.com","gyas tazs okaf ckux")


username=input("Username the username >>")
email=input("Email the email >> ")
message=input("Enter message >>")

#                  from                to            message
server.sendmail("gnnandan7@gmail.com",email,f"Hello, {username} {message}")


print("Email sent successfully!")