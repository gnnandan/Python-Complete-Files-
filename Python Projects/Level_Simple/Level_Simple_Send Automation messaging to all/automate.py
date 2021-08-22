import smtplib as smtplib
import pywhatkit
import requests
import json


# automate to mail
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("gnnandan7@gmail.com","gyas tazs okaf ckux")
username=input("Username the username >>")
email=input("Email the email >> ")
message=input("Enter message >>")
server.sendmail("gnnandan7@gmail.com",email,f"Hello, {username} {message}")


# automate to what's app
hr=20
min=51
msg=f"Hello {username} This is automate message using python By Nandan G N"
w=5
pywhatkit.sendwhatmsg(time_hour=hr,time_min=min,wait_time=w,phone_no="+919108901507",message=msg)
print("What's App Message Sent Successfully!")

# automate to SMS
url="https://www.fast2sms.com/dev/bulk"
my_data={'sender_id':'Private Message Nandan GN','message':f'Hello {username} This is automate message using python By Nandan G N','language':'english','route':'p','numbers':9108901507}
headers={

"authorization":"ykO4x1UBrh0KscDW9n6lH8bvTX5jMzGt7IYwidepmNoQ2ZqgCSxNPI28jl7Uas9mRMnF06GWzXZDHoqy",
"Content-Type":"application/x-www-form-urlencoded","Cache-Control":"no-cahce"
}

response=requests.request("POST",url,data=my_data,headers=headers)
returned_msg=json.loads(response.text)
print(returned_msg)

