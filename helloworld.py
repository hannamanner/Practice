
y = "Good day!"
print(y)
x = input("How many customers in line? ")
if x>1:
    print("Please take a seat!")

"""
How would you go about putting a pause here, like it takes a while for a 
patient to get called to the pharmacist desk?
"""

prescription = input("Do you have a prescription?: ")
patient = input("Status of patient: ")

if prescription == "Yes" and patient == "alive":
    print("New prescription") 
else:
    print("No prescription")