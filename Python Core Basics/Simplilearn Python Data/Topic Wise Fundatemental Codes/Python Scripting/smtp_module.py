import smtplib


# ! sending mail using python
smtpobj = smtplib.SMTP('smtp.gmail.com',587)
#             domain,port_number

# sending mail
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login()