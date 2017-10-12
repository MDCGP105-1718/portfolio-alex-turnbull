annual_salary = float(input("Enter your annual salary: "))
portion_save = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi annual raise: "))

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
    if (totalMonths % 6 == 0):
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary = annual_salary/12
    current_savings += current_savings*r + portion_save*monthly_salary
    if (current_savings > deposit):
        reachedDeposit = True


print("\nNumber of months:",totalMonths)
