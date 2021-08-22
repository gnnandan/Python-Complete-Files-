# libraries 
import os
import random
import smtplib

def auto_mail():
    
    # take [user ,email, message]
    user=input("Enter the username >> ")
    email=input("Enter the email >> ")
    message=(f"Hello {user}, How are you {user} this is automation test mail using 'PYTHON' ")
    
    # take smtp_mail and port(smtp.gmail.com,port)  
    s=smtplib.SMTP('smtp.gmail.com',587)
    
    # implement and starttls
    s.starttls()
    
    # login with the 16 digit Google app password
    s.login("gnnandan7@gmail.com",'gyas tazs okaf ckux')
    
    # times to send the same email 
    times=0
    while times < 10:
        times+=1
        s.sendmail("Hello",email,message)
    print("Email sent Successfully!")
    
auto_mail()