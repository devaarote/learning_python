from multipledispatch import dispatch


class test_calculator:
    @dispatch(int,int)
    def add(self,a,b):
        return a + b
    

    @dispatch(float,float)
    def add(self,a,b):
        return a + b
    
    @dispatch(int,float)
    def add(self,a,b):  
        return a + b
    
    @dispatch(float,int)
    def add(self,a,b):
        return a + b
    
c1=test_calculator()
print(c1.add(10,20))            #integer addition
print(c1.add(10.5,20.3))        #float addition
print(c1.add(10,20.5))          #int and float addition
print(c1.add(10.5,20))          #float and int addition 

