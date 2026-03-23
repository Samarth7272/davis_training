# Question 41: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount


def calculate_final_price(price, discount):
    return price - (price * discount / 100) 

price= float(input("Enter price: "))
if price < 0:
    print("Invalid price, try again")
else:
    discount= float(input("Enter discount percentage: "))
    if discount < 0 or discount > 100:
        print("Invalid discount percentage, try again")
    else:
        print(calculate_final_price(price, discount))   