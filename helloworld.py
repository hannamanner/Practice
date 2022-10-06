
y = "Good day!"
print(y)
x = int(input("How many customers in line? "))
if x > 1:
    print("Please take a seat!")
print("Next, please!")

prescription = input("Do you have a prescription? (Yes/No): ")

if prescription == "No" or prescription == "no":
    print("I'm sorry, I can't help you then.")
    quit()
patient = input("Status of patient: ")

if prescription == "Yes" and patient == "alive":
    print("New prescription") 
else:
    print("No prescription")