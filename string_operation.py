str1="    Devendra Arote   "

print(len(str1))

print(str1.upper())

print(str1.lower())

#del str1

# print(str1)     NameError: name 'str1' is not defined. Did you mean: 'str'?

str2="Learning Python is fun in Fortune cloud"
print(str2)

print(str2.replace("fun","Amazing"))

print(str1.strip())


a="Devendra"
b="pimpri"

print(f"My name is {a} and i am live in {b}")

c='I am {} and i am from {}'.format(a,b)

print(c)