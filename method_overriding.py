#implementing parent method into class with new defininition using 


class vehical:
    def getcolor(self):
        print("Color of vehical is white")
class car(vehical):
    def getcolor(self):
        print ("car color is red")

c1=car()
c1.getcolor()
v1=vehical()
v1.getcolor()
