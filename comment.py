# this program is used for printing personal information
print("Devendra Arote")
print("I am from Ahilyanagar") #this statement should print
'''This is multiline comment example 
in python program'''

print("Thankyou")

var="Sample"    #Valid 
_var1="printing"  #Valid
# 1var="test" invalid 
# var one="var one" invalid

#Single value to multiple layer
var=var1=var2=var3=15

print(var)
print(var1)
print(var2)
print(var3)

#multiple value to multiple variable
v1,v2,v3=101,"Rahul",19.2

print(v1)
print(v2)
print(v3)


#type casting
var=9
var2=var/4
print(var2)      #Implicit Typecasting
var2=int(var2)
print(var2)      #Explicit Typecasting

var_i=10
var_s="Devendra"
var_b=True
var_l=[1,2,3,4]
var_f=13.5

print(type(var_i))
print(type(var_s))
print(type(var_b))
print(type(var_l))
print(type(var_f))