"""age=int(input("Enter your age: "))
if age < 18:
    raise Exception("age less than is not elible for voting")
else:
    print("elible for voting")"""

num=[1,2,3,4,5]
if len(num)>3:
    raise Exception("length of list is less or equal than 3")
else:
    print("length of list:",len(num))

