# Question 1: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount

price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

discount_amount = (price * discount) / 100
final_price = price - discount_amount

print("Final Price:", final_price)