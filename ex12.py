def hotel_cost(nights):
    return 70.0*nights

def plane_ticket(city, classType):
    locations = {
                "New York": 2000,
                "Auckland": 790,
                "Venice": 154,
                "Glasgow": 65
                }
    return locations[city] * classType

def rental_car_cost(days):
    costPerDay = 30
    totalCost = costPerDay*days
    if days > 7:
        totalCost -= 50
    elif days >3:
        totalCost -= 30
    return totalCost

def total_cost(city, classType, days):
    finalCost = 0
    finalCost += hotel_cost(days)
    finalCost += rental_car_cost(days)
    finalCost += plane_ticket(city, classType)

    return finalCost
print(total_cost(str(input("What city to travel to? ")),float(input("What class for your flight? ")),int(input("Number of days/nights: "))))