class addtion:
    def add(self,no1,no2):
        return no1+no2  
class substraction:
    def sub(self,no1,no2):
        return no1-no2
class multiplication:
    def mul(self,no1,no2):
        return no1*no2
class division:
    def div(self,no1,no2):
        return no1/no2
class calculator(addtion,substraction,multiplication,division):
    def mod(self,no1,no2):
        return no1%no2
calc=calculator()
print("Addition:",calc.add(10,5))   
print("Substraction:",calc.sub(10,5))
print("Multiplication:",calc.mul(10,5))
print("Division:",calc.div(10,5))
print("Modulus:",calc.mod(10,5))    


print(isinstance(calc,addtion))
print(issubclass(calculator,division))  
