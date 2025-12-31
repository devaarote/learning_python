class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

        #public method
    def display(self):
        print(f'Car Brand: {self.brand}, Model: {self.model}')


c1=car("Toyata","Taisor")

# c1.display()

# print("Car Brand:",c1.brand)
# print("Car Model:",c1.model)

class subclasstest(car):
    def showdetails(self):
        print("car brand:",self.brand)
        print("car model:",self.model)
        self.display()
c1=subclasstest("Honda","Civic")
c1.showdetails()    

class outsidetest:
    pass
s1=car("Ford","Mustang")
print(s1.brand)
print(s1.model)
s1.display()    