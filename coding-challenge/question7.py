# Question 7: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible


age = int(input("Enter age: "))

result = "Eligible" if age >= 18 else "Not Eligible"
print(result)