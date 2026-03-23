# Question 26: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount

n = int(input("Enter number of items: "))

for i in range(n):
    p = float(input("Enter price: "))
    d = float(input("Enter discount percentage: "))

    print(p - (p * d / 100))