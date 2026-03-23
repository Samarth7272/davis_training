# Question 23: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount

price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

if price > 0 and 0 <= discount <= 100:
    print(f"Final price after discount: {price - price*discount/100}")
else:
    print("Invalid input")