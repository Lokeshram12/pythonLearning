class Car:
    def __init__(self,model,brand):
        self.__brand=brand
        self.model=model
    
    def get_brand(self):
        return self.__brand + " !! "

    def fullName(self):
       return f"{self.model}{self.get_brand}"

# Inheritance
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size


myCar=Car("abc","abd")
print(myCar.model , myCar.get_brand)
print(myCar.fullName())
myTesla=ElectricCar("tesla","abc","85kWH")
print(myTesla.battery_size)
print(myTesla.get_brand())

# class variable/static
#  @staticmethod
