def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index=email.index("@" +old_domain)
        new_email=email[:index] + "@" +new_domain
        return new_email
    return email

print(replace_domain("codershandbook7@gmail.com",'codershandbook.in',"Coderscommunity.com"))