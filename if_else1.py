marks=int(input("Enter your marks: "))

if marks <= 40 and marks > 0:
    print("You are failed")
elif marks<=60 and marks > 40:
    print("Second Class")
elif marks<=75 and marks > 60:
    print("First Class")
elif marks<=75 and marks > 100:
    print("Distinction")
else:
    print("Invalid Marks")

print("rest of the code")

