s1={1,2,3}
s2={3,4,5,6}
print("Set s1: ",s1)
print("Set s2: ",s2)
print("symmentric difference of s1 and s2 : ",s1.symmetric_difference(s2))

#intersection_update()- Intersection of two sets and update the first set with the result
s1.intersection_update(s2)  
print("After intersection_update of s1 with s2, s1: ",s1)

s3={1,2,3}
s4={3,2}
#difference_update()- Difference of two sets and update the first set with the result
print("Set s3: ",s3)
print("Set s4: ",s4)
s3.difference_update(s4)  
print("After difference_update of s3 with s4, s3: ",s3)                                                 
