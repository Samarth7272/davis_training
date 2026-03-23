# Question 36: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount

price = float(input())
d = float(input())

if price > 1000:
    price = price - (price * d / 100)

print(price)