"""[summary]
        "attributes": Data describing the object
object =    
        "behaviour": Methods on the attributes
"""


class data:
    def __init__(self,name,age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def person(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My gender is:",self.gender)
    
    def education(self, email, college, phone):
        self.person()
        self.email= email
        self.college = college
        self.phone = phone
        print(f"{self.name}, my email is {self.email}")
        print(f"My college is {self.college}")
        print(f"My phone is {self.phone}")

name = input("Please specify your name:")
age = int(input("Please Specify your age:"))
gender = str(input("Please specify your gender:"))
email = str(input("Please specify your email:"))
college = str(input('Enter your college:'))
phone = int(input("Enter your phone:"))
info = data(name = name,age= age, gender = gender) 
info.education(email = email, college = college, phone = phone)
                