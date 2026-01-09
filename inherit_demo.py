class animal:                   #Parent class
    def speak(self):
        print("The animal makes a sound.")
    X=50

class cow(animal):               #Child class inheriting from animal
    def eat(self):
        print("The cow eats grass.")
    def speak(self):               #Overriding the speak method
        print("Cow making sound ba ba")

    
c1=cow()
c1.speak()
c1.eat()
print("Value of X from parent class:",c1.X)
a1=animal()
a1.speak()
    
