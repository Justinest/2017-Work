temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print ("It is cold outside")
else:
    print("It is not hot outside")
print("Done")


temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 120:
    print("It is hot outside")
elif temperature > 90:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is ok outside")
print("Done")

# Comparisons using string/text
# Note, this example does not work when running under Eclipse
# because the input will contain an extra carriage return at the
# end. It works fine under IDLE.
userName = input("What is your name? ")
if userName == "Paul" or userName == "Mary":
    print("You have a nice name.")
else:
    print("Your name is ok.")
    

user_name = input("What is your name? ")
if user_name.lower() == "paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")
    