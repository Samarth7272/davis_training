# Question 6: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount

def calculate_discount(price, discount):
    return price - (price * discount / 100)

p = float(input("Enter price: "))
d = float(input("Enter discount %: "))

result = calculate_discount(p, d)
print("Final Price:", result)