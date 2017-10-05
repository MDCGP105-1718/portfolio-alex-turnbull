annual_salary = float(input("Enter your annual salary: "))
portion_save = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_deposit = 0.2
current_savings = 0.0
r = 0.04

deposit = total_cost*portion_deposit
monthly_salary = annual_salary/12
current_savings += portion_save*monthly_salary

totalMonths = 0
reachedDeposit = False
while (not reachedDeposit):
    totalMonths += 1
    current_savings += current_savings*r
    if (current_savings > deposit):
        reachedDeposit = True


print("\nNumber of months:",totalMonths)
