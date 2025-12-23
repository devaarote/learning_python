class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

car1 = Car("Tata", "Nexon")
car2 = Car("Ford", "Mustang")
car3 = Car("Toyota", "Camry")   

car1.drive()
car2.drive() 
car3.drive()    
