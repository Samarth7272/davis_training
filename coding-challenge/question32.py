# Question 32: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible
age = int(input("Enter your age: "))

#display the input age
print(f"Your age is: {age}")
# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are eligible to vote.")
    
elif age < 0:
    print("Invalid age entered. Age cannot be negative.")
    
else:
    print("You are not eligible to vote.")