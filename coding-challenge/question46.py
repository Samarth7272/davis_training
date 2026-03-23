# Question 46: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount


p = float(input("Enter price: "))
d = float(input("Enter discount: "))

print(f"Final price after discount: {(lambda p,d: p-p*d/100)(p,d)}")