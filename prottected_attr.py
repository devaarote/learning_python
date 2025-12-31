class car:
    def __init__(self,brand,model):
        self._brand=brand      #protected attribute
        self._model=model

        #protected method
    def display(self):
        print(f'Car Brand: {self._brand}, Model: {self._model}')

        def show(self):
            self.display()


# c1=car("Toyata","Taisor")
# c1.display()   


class subclasstest(car):
    def showdetails(self):
        print("car brand:",self._brand)
        print("car model:",self._model)
        self.display()  
s1=subclasstest("Honda","Civic")
s1.showdetails()

class outsidetest:
    pass                                                
s1=car("Ford","Mustang")
print("Car Brand:",s1._brand)
print("Car Model:",s1._model)
s1.display()