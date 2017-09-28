my_name = 'Alex Turnbull'
my_age = 18
my_height = 73 #inches
my_weight = 121 #pounds
my_eyes = 'Blue'
my_hair = 'Brown'
is_heavy = my_weight > 3000

height_in_cm = round(my_height * 2.54,2)
weight_in_kg = round(my_weight * 0.45359237,2)

print(f"Let's talk about {my_name}.")

print(f"He is {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"It is {is_heavy} that he is overweight.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His height in cenimeters is {height_in_cm}.")
print(f"His weight in kilograms is {weight_in_kg}.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I got {total}")
