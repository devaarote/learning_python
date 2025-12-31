class a:
    def details(self,a):
        print("Details from class A:",a)
    
    def details(self,a,b):
        print("a=",a)
        print("b=",b)


a1=a()
a1.details(10,20)
a1.details(11,22)
#Note: In Python, the last defined method will override any previous definitions with the same name

class a:
    def details(self,a,b=0,c=0):
        return a+b+c
    
a1=a()
print(a1.details(10))
print(a1.details(0,20))
print(a1.details(0,0,30))

class b:
    def sum(self,*args):
        return sum(args)
b1=b()
print(b1.sum(10,20))    
print(b1.sum(10,20,30,40))
print(b1.sum(5,15,25,35,45,55))
