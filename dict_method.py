# Update()-it will update the a dictionary with another dictionary or with key-value pairs
d1={"name": "Alice",
    "age": 30,  
    "Gender": "Female"
    }
d2={"city": "New York",
    "country": "USA"}

print("Dictionary d1 before update: ",d1)
d1.update(d2)  # updating d1 with d2
print("Dictionary d1 after update: ",d1)

#keys()-it will return all the keys of the dictionary

print("Keys of d1: ",d1.keys())

#formkeys()-it will create a new dictionary with the specified keys and values set to None or to a specified value
#items()-it will return all the key-value pairs of the dictionary as tuples in a list   
#setdefault()-it will return the value of a specified key. If the key does not exist, it will insert the key with a specified value
#values()-it will return all the values of the dictionary
#pop()-it will remove and return the value of a specified key
#popitem()-it will remove and return the last inserted key-value pair as a tuple
#get()-it will return the value of a specified key
#printing the keys of d1 using keys() method



