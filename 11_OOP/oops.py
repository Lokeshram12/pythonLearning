class Car:
    def __init__(self,model,brand):
        self.brand=brand
        self.model=model

myCar=Car("abc","abd")
print(Car)
print(myCar)
print(myCar.model , myCar.brand)