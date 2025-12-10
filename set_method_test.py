#Adding data to existing set using add() add one element at a time in set
# update() add multiple element at a time in set
s1={"math","science","english"}
print("Original set: ",s1)
s1.add("history")
print("set after adding one element using add(): ",s1)
s1.update(["art","geography","biology"])
print("set after adding multiple element using update(): ",s1)

#creating copy of set using copy()
s2={1,2,3,4,5}
print("Original set s2: ",s2)
s3=s2.copy()
print("Copy of set s2 into s3: ",s3)

#removing element from set using remove() and discard()
s4={"male","female","other","Nothing"}
print("Original set s4: ",s4)
s4.remove("Nothing")
print("set s4 after removing element using remove(): ",s4)
s4.discard("other")
print("set s4 after removing element using discard(): ",s4)

# removing and returning a random  element using pop()
s4.pop()
print("set s4 after removing element using pop(): ",s4)

# clearing all elements from set using clear()
s4.clear()  
print("set s4 after clearing all elements using clear(): ",s4)

# deleting entire set using del
del s4  
#print(s4)  # it will give error because set s4 is deleted