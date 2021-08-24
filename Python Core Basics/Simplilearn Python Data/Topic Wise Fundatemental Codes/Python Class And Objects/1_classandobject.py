# Note
# ? object 
    # ! every instance is an object 
# ? class
    # ! a class is a blueprint of similar objects

#  Note creating a class
class person:
    # ! defining a feature that this class defines (we use constructor)
    def __init__(self):
        # ! features are name, gender, age and this feature should be call suing the constructor "self."
        self.name  = input("Please enter name:")
        self.gender = input("Please enter your gender:")
        self.age = int(input("Please enter your age:"))
        
    # ! defining the behaviours/ methods
    def talk(self):
        print(f"Hello i'm {self.name}")
        
    #  ! another method
    def vote(self):
        if self.age < 18:
            print(f"Sorry {self.name}, you are not eligible to vote")
            print("Thank You")
        else:
            print(f"Thank You {self.name}, Move ahead and stay safe!")

# ! creating an object to call a class
obj = person()

# ! calling the members of object
obj.talk()
obj.vote()
