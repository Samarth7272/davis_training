# Question 27: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible

def check(age):
    return age >= 18

age = int(input("Enter age: "))
print("Eligible" if check(age) else "Not Eligible")
