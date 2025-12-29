class vehical:
    def getColor(self):
        print("Color of vehical")
class FourWheeler(vehical):
    def FourWheels(self):
        print("Four wheels is running")

class swift(FourWheeler):
    def TwoWheelDrive(self):
        print("It is Two wheeel drive") 

s1=swift()
s1.getColor()
s1.TwoWheelDrive()
s1.FourWheels()
