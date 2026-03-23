# Question 22: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible

n = int(input("Enter number of people: "))
results = []

for i in range(n):
    age = int(input("Enter age: "))
    if age >= 18:
        results.append("Eligible")
    else:
        results.append("Not Eligible")

print(results)

