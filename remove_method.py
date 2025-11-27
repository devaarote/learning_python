list=[12,34,56,78]
list1=[98,76,54,32]

list1.insert(7,14)  
print("after Insert",list1)

list1.remove(98)
print("after remove: ",list1)

list.clear() #remove all element in list

print("index of 76:", list1.index(76)) #IT WILL GOVE INDEX OF SPECIFIC ELEMENTS

print("count of 20",list1.count(76)) #it will give us count


list1.sort()
print("After sort",list1)

list1.reverse()

print("After reverse",list1)


