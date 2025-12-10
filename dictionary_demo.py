d1={"id":1,"city":"mumbai","Organization":"Fortune cloud","marks":93.00}
print("Dictionary d1: ",d1)

#Ways of creting dictionarys
# empty dictionary
# {}
# dict()
d2={}
print("Empty dictionary d2: ",d2)   
print("Type of d2: ",type(d2))
d2={"name":"John","age":30,"city":"New York"}
print("Dictionary d2: ",d2) 
d3=dict(id=2,city="Pune",Organization="Tech Solutions",marks=88.50)
print("Dictionary d3: ",d3)


d3={"name":"Alice","age":25,"city":"Los Angeles"}
print("d3: ",d3)
print("Accessing name from d3: ",d3["name"])
print("Accessing age from d3: ",d3["age"])  
print("Accessing city from d3: ",d3["city"])

d3["country"]="USA"
print("After adding country to d3: ",d3)    

d3["state"]="California"
print("After adding state to d3: ",d3)

# how to delete a key-value pair from dictionary
# del - keyword
del d3["state"]     
print("After deleting state from d3: ",d3)

# 2 method - pop()
pop_value = d3.pop("country") 
print("Popped value: ", pop_value)
print("After popping country from d3: ",d3) 

# 3 method - popitem() - removes the last inserted key-value pair
d4=d3.popitem()
print("Popped item: ", d4)
print("After popitem() from d3: ",d3) 

d5={"name":"Bob","age":28,"city":"Chicago"}
print("Dictionary d5: ",d5) 
d5.clear()
print("After clearing all items from d5: ",d5)

# Adding multiple items to dictionary using update()
d6={"name":"Eve","age":22}  
print("Dictionary d6 before update: ",d6)
d6.update({"city":"Miami","country":"USA"}) 
print("Dictionary d6 after update: ",d6)

# update a element
d6.update({"age":23})   
print("Dictionary d6 after updating age: ",d6)

# element in dictionary find
print("no of elements in d6: ",len(d6))
