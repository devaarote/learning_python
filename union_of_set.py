s1={1,2,3,6}
s2={4,5,1,2,3}
print("Set s1: ",s1)
print("Set s2: ",s2) 
print("Union of s1 and s2 using '|' operator: ",s1 | s2)   
print("Union of s1 and s2 using union() method: ",s1.union(s2))
#Intersection of sets
print("Intersection of s1 and s2 using '&' operator: ",s1 & s2)   
print("Intersection of s1 and s2 using intersection() method: ",s1.intersection(s2))

#Difference of sets
print("Difference of s1 and s2 using '-' operator: ",s1 - s2)   
print("Difference of s1 and s2 using difference() method: ",s2.difference(s1))