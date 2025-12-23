class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def display(self):
        print(self.id," ",self.name)

e1=employee("Devendra",101)
e2=employee("Rahul",102)

e1.display()
e2.display()    
