# Question 16: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount

n = int(input("Enter number of items: "))
total = 0

for i in range(n):
    price = float(input("Enter price: "))
    total += price

discount = float(input("Enter discount %: "))
final = total - (total * discount / 100)

print("Final Bill:", final)