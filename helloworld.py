import time
print("Good day!")

while True:
    
    try:
        x = int(input("How many customers in line? "))
    except ValueError:
        print("... My dude.")
        continue
    if x <1 or x > 20:
        print("There's no way!")
    else:
        break

if x > 1:
    print("Please take a seat!")
    doze = 5
    x = x-1
while x > 2:
    x = x-1
    time.sleep(doze)
    print(f"Just a bit longer, only {x} more people before you...")
time.sleep(doze)
print(f"Just a bit longer, only 1 more person before you...")
time.sleep(doze)
print("Next, please!")

prescription = input("Do you have a prescription? (Yes/No): ")
if prescription.lower() != "yes":
    print("I'm sorry, I can't help you then.")
    quit()
patient = input("Status of patient: ")

if patient.lower() == "alive":
    print("Here's your prescription, have a nice day!") 
else:
    print("What on Earth are you doing here then?!")