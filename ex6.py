name = input("What is your name? ")
age = int(input("How many years old are you? "))
height = float(input("What is your height in cenimeters? "))
weight = float(input("What is your wieght in kilograms? "))
eyeColour = input("What colour are your eyes? ")
hairColour = input("What is your hair colour? ")

adult = False
tall = False
heavy = False

if (age >= 18):
    adult = True
if (height >= 180):
    tall = True
if (weight >= 100):
    heavy = True

print(f"\nHere we have {name}, they are {age} years old so it is {adult} that they are an adult.\nThey {height}cm tall, which makes it {tall} that they are above the average height\nThey weigh {weight}kg meaning it is {heavy} that they are above average in their weight.\nThey have {eyeColour} eyes and {hairColour} hair.")
