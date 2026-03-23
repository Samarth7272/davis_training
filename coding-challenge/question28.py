# Question 28: Calculate electricity bill based on units consumed.
# Input: Enter unitsOutput: Total bill amount

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

calc = lambda p, d: p - p*d/100
print(f"Final price after discount: {calc(price, discount)}")
