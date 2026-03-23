# Question 38: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount


units = int(input("Enter units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100*5 + (units-100)*7
else:
    bill = 100*5 + 100*7 + (units-200)*10
print("Total bill:", bill)