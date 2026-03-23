# Question 21: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount

def discount(price, d):
    return price - (price * d / 100)

while True:
    price = float(input("Enter price: "))
    d = float(input("Enter discount: "))

    print("Final Price:", discount(price, d))
