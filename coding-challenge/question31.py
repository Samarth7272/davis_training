# Question 31: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount

total_bill = float(input("Enter the total bill amount: "))
# Check the total bill amount and apply the appropriate discount
if total_bill > 1000:
    discount = total_bill * 0.10  # 10% discount
    discount_percentage = 10
elif total_bill > 500:
    discount = total_bill * 0.05  # 5% discount
    discount_percentage = 5
else:
    discount = 0  # No discount
    discount_percentage = 0
    
# Calculate the final bill amount after applying the discount
final_bill = total_bill - discount
# Print the discount percentage and the final bill amount
print(f"Discount Percentage: {discount_percentage}%")
print(f"Final Bill Amount after discount: {final_bill:.2f}")