def cal_square(num):
    res=num*num
    return res
    print("this line is not executed") #this line is not executed

print("Rest of the code after function")
sq_of_no=cal_square(25)
print("square is:",sq_of_no)

def greet():
    print("Hello User") 

print("rest of the code")
res=greet()
print("result is:",res )
def empty():
    pass
print("Result:",empty())

