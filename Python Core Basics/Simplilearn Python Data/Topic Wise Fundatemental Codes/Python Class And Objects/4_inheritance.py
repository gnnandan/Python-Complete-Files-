# OOPS concept 
# ! inheritance in python

class car: # ! parent class
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed
        
    def type(self,type,brand):
        self.type = type 
        self.brand = brand
        print(f"Sir, You choosed {self.type}")
        if self.type == 'SUV':
            if self.brand == "TATA":
                print("We have Rangerover its a great option")
            elif self.brand == "MAHINDRA":
                print('We have Thar')
                print("We have XUV500")
                print("We have XUV700")
                print("We Have Scorpio")
        elif self.type == 'HATCHBACK':
            if self.brand == "TATA":
                print("We have Nexon its a great option")
            elif self.brand == "Hyundai":
                print('We have i20')
                print("We have i10")         
        else:
            print("Thank You Sir Visit Again.....!")

class price(car): # ! child class
    def __init__(self, brand, color, speed):
        super().__init__(brand, color, speed)
    
    def price_data(self):
        if self.type == 'SUV':
            print("Price start from 10Lakhs")
        elif self.type == 'HATCHBACK':
            print("Price start from 7Lakhs")
            
color = input("Enter the color:")
speed = input("Enter the speed:")
brand = input("Please choose a brand:")
type = input("Enter the type:")
cars = car(brand = brand, color = color, speed=speed)
prices = price(brand = brand, color = color, speed=speed)
cars.type(type=type,brand=brand)
prices.price_data()