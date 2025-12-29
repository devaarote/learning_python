class vehical:
    def __init__(self,id,name,chesis_no):
        self.id=id
        self.name=name
        self.chesis_no=chesis_no


v1=vehical(101,"BMW","CH1234")
print(getattr(v1,'chesis_no',0))
setattr(v1,"chesis_no","CH5678") #set attribute chesis_no
print(getattr(v1,'chesis_no',0)) #get attribute chesis_no   
print(hasattr(v1,"name"))  #has attribute name
print(hasattr(v1,"model")) #has attribute model #False

delattr(v1,"name")#delete attribute name
print(v1,"name")   #error # This will raise AttributeError since 'name' attribute is deleted
        