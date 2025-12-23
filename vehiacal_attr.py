class vehical:
    def __init__(self,id,name,chesis_no):
        self.id=id
        self.name=name
        self.chesis_no=chesis_no


v1=vehical(101,"BMW","CH1234")
print(getattr(v1,'chesis_no',0))
setattr(v1,"chesis_no","CH5678")
print(getattr(v1,'chesis_no',0))
print(hasattr(v1,"name"))
print(hasattr(v1,"model"))

delattr(v1,"name")#delete attribute name
print(v1,"name")  # This will raise AttributeError since 'name' attribute is deleted
        