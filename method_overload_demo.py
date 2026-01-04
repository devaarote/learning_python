from functools import singledispatchmethod

class test_calculator:
    @singledispatchmethod
    def add(self,a,b):
        return a + b
    
    @add.register(int)
    def _(self,a: str, b: str):
        return a + b
    
    @add.register(float)
    def _(self,a: float, b: float):
        return a+b
    
c1=test_calculator()
print(c1.add(10,20))            #integer addition
print(c1.add(10.5,20.3))        #float addition
print(c1.add("Hello ","World")) #string concatenation
print(c1.add([1,2],[3,4]))     #list concatenation
