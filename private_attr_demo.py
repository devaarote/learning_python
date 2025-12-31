class car:
    def __init__(self,brand,model):
        self.__brand=brand      #private attribute
        self.__model=model

        #private method
    def display(self):
        print(f'Car Brand: {self.__brand}, Model: {self.__model}')

        def show(self):
            self.display()


# c1=car("Toyata","Taisor")
# c1.display()   


class subclasstest(car):
    def showdetails(self):
        print("car brand:",self.__brand)
        print("car model:",self.__model)
        self.display()  
s1=subclasstest("Honda","Civic")
# s1.showdetails()

class outsidetest:
    pass                                                
s1=car("Ford","Mustang")
print("Car Brand:",s1.__brand)
print("Car Model:",s1.__model)
s1.display()