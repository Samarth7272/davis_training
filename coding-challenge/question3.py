# Question 3: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Total Bill:", bill)