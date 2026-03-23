# Input number
num = int(input("Enter a positive number: "))

# Initialize the greatest digit
greatest = 0

# Loop through all digits
while num > 0:
    digit = num % 10        # Get the last digit
    if digit > greatest:
        greatest = digit    # Update greatest if current digit is bigger
    num = num // 10         # Remove the last digit

print("The greatest digit is:", greatest)