
y = "Good day!"
print(y)
x = input("How many customers in line? ")
x_2 = int(x)
if x_2 > 1:
    print("Please take a seat!")
print("Next, please!")

prescription = input("Do you have a prescription?: ")
patient = input("Status of patient: ")

if prescription == "Yes" and patient == "alive":
    print("New prescription") 
else:
    print("No prescription")