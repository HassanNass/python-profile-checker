name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA (0-5): "))
field = input("what is your field of interest?: ")
graduated = input("Have you graduated? (yes/no): ")

graduated = graduated.lower()

if graduated == "yes" or graduated == "no":
    print("Name              : ", name)
    print("age               : ", age)
    print("GPA               : ", gpa)
    print("Field of Interest : ", field)
    print("Graduated         : ", graduated)
    
    if age < 25 and gpa >= 3.5 and graduated == "yes":
        print("You are eligible for a scholarship")
    elif age < 30 and gpa >= 2.5:
        print("You are eligible for an internship")
    else:
        print("Please apply again later.")
else:
    print("Please answer with 'yes' or 'no'")