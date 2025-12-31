from abc import ABC, abstractmethod

class shape(ABC):

    @abstractmethod
    def start(self):
        pass
    
    
    def details(self):         
        print("Printing Details")

class circle():
    def start(self):
        print("started drawing circle")


c1=circle()
c1.start()

class square(shape):
    def start(self):
        print("started drawing square")
s1=square()
s1.start()
s1.details()