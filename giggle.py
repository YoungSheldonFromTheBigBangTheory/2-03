

name = input("What is your name?")
age = int(input("How old are you?"))
bday = str(input("Did you have your birthday? yes or no?"))

def agefunction():
    if bday == "yes" and "Yes":
        h = 2023 - age
        print ("you are",h,"years old",(name))
    else:
        h = 2022 - age
        print ("you are",h,"years old",(name))

agefunction()

