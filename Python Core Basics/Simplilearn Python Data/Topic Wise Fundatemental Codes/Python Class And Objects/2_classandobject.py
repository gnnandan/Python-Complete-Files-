import random as ra

company = ['TESLA','JIO','TATA','GOOGLE','MICROSOFT']
company = ra.choice(company)
# print(company)
class mydata:
    # ! creating a constructor for it 
    def __init__(self):
        self.name  = input("Enter the name:")
        self.gender = input("Enter the gender:")
        self.age = int(input("Enter the age:"))
        
    # ! creating the methods
    def qualification(self):
        self.inputs = input(f"{self.name} Please enter your reacent education:")
        self.branch = input(f"{self.name} Please enter your {self.inputs} branch:")
        self.result = int(input(f"{self.name} Please enter your {self.branch} CGPA or %:"))

    def domain_allot(self):
        if self.inputs == 'BE' or self.inputs == 'be':
            print(f"Dear {self.name} you alloted as a 'Software Developer'")
            
    def opportunity(self):
        if self.age > 20 and self.result > 55 or self.result > 5:
            print(f"Welcome to onboard Mr.{self.name} and Thanks for Choosing us\n Regards {company}:")
            self.email = input(f"{self.name} please give your email to send further details:")
            self.phone = input(f"{self.name} please give your phone to send further reference:")
        else:
            print(f"Dear {self.name} take time to prepare yourself and be ready for assesments")
            
    def confirm_data(self):
        print(f"Your Name: {self.name}")
        print(f"Your age: {self.age}")
        print(f"Your gender: {self.gender}")
        print(f"Your education: {self.inputs}")
        print(f"Your result: {self.result}")
        print(f"Your email: {self.email}")
        print(f"Your phone: {self.phone}")
        cross_check = input("Please check below data once and give 'yes' or 'no'")
        if cross_check == "yes":
            print(f"Your offer letter will be sent to your email: {self.email}:")
            
            # ! Calling one method from another method 
            self.domain_allot()
        
# creating an object
data = mydata()
data.qualification()
data.opportunity()
data.confirm_data()