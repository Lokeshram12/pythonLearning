class Car:
    def __init__(self,model,brand):
        self.brand=brand
        self.model=model
    
    def fullName(self):
       return f"{self.model}{self.brand}"
# Inheritance
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size



myCar=Car("abc","abd")
print(Car)
print(myCar)
print(myCar.model , myCar.brand)
print(myCar.fullName())
myTesla=ElectricCar("tesla","abc","85kWH")
print(myTesla.battery_size)
