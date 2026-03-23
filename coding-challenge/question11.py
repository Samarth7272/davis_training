# Question 11: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount

while True:
    price = float(input("Enter price: "))
    discount = float(input("Enter discount %: "))

    if discount >= 0 and discount <= 100:
        break
    else:
        print("Invalid discount, try again")

final_price = price - (price * discount / 100)
print("Final Price:", final_price)