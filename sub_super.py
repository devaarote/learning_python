class A:
    def method(self):
        print("merthod of class A")
class B(A):
    def method(self):
        print("merthod of class B")    

print("B is subclass of A?",issubclass(B,A))