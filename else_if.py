no1=int(input("Enter the first number"))
no2=int(input("Enter the second number"))
no3=int(input("Enter the third number"))

if no1>no2 and no1>no3:
    print("no1 is largest number")
elif no2>no1 and no2>no3:
    print("no2 is largest number")
elif no3>no1 and no3>no2:
    print("no3 is largest number")
else:
    print("Invalid Number")

print("Rest of the code")
