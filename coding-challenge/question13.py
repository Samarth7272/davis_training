# Question 13: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount

def bill_calc(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return units * 7
    else:
        return units * 10

u = int(input("Enter units: "))
print("Total Bill:", bill_calc(u))