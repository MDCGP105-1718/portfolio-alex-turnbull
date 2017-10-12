#Bisection Algorithm
#cube = 27
#epsilon = 0.01
#num_guesses = 0
#low = 0
#high = cube
#guess = (high + low)/2.0
#while (abs(guess**3 - cube) >= epsilon):
#    if (guess**3 < cube):
#        low = guess
#    else:
#        high = guess
#    guess = (high + low)/2.0
#    num_guesses += 1
#
#print ("Number of Guesses =", num_guesses)
#print (guess, "is close to the cube root of", cube)
#######################################################


annual_salary = float(input("Enter the starting salary: "))
cost_of_house = 1000000.0
down_payment = cost_of_house*0.25
annual_rate = 0.04
semi_annual_raise = 0.07
number_of_months = 36
current_savings = 0
monthly_salary = annual_salary/12

for i in range(1,37):
    if i % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary = annual_salary/12
    current_savings += monthly_salary

print (current_savings)

epsilon = 100
low = 0
high = 10000
midpoint = (high - low)/2.0
num_guesses = 0
while (abs(current_savings*(midpoint/10000) - high) >= epsilon):
    if (current_savings*(midpoint/10000) < down_payment):
        low = midpoint
    else:
        high = midpoint
    midpoint = (high + low)/2.0
    num_guesses += 1
    if num_guesses == 100:
        break

print (num_guesses)
print (midpoint/10000)
