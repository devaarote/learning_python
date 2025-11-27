t1=()
t2=(12,13,14)
t3=(10,"FCT",13.4,[1,2,3])
t4=({1:2,2:4,3:6},(5,4,3,6))

print(t1)
print(t2)
print(t3)
print(t4)
print("t2[1]: ",t2[1])
print("t2[-2]: ",t2[-2])



# how to slice the tupple
t5=[87,43,41,22,21,78,18,4]
print("Data of t5 between index 1 to 5: ",t5[1:5])  # Slice of tuple prirnt[startindex:endindex]
print("Data of t5 between index 0 to -4: ",t5[:-4])

#del t5      # delete a tuple
print(t5.count(22))  #count a element 
print(t5)

t6=["India","UK","USA","France","Japan","India","UK"]
print(t6)
print("Count of India: ",t6.count("India"))
print("Index of India: ",t6.index("India"))

t7=(10,20,30,40)
print("Data of t7: ",t7)

t8=t7+(50,)

print("Data of t8: ",t8)

l1=list(t7)
print("tuple Converted into list",l1)


l2=[1,2,3,4,5]
t1=tuple(l2)
print("list Converted into tuple",t1)