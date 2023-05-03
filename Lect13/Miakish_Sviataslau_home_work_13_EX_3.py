class Car:
    def __init__(self, vin):
        print("Ordinaty __init__ was called for", vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print("Class method was called")
        _car = cls(vin)
        _car.brand = brand
        return _car
    
car1 = Car("ABC123")
car2 = Car.including_brand("DEF567", "Audi")

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)