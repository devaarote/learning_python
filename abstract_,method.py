from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Child class
class Circle(Shape):

    def start(self):
        print("Circle started")

    def stop(self):
        print("Circle stopped")


# Object creation
c = Circle()
c.start()
c.stop()
