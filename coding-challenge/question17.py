# Question 17: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible

n = int(input("Enter number of people: "))
count = 0

for i in range(n):
    age = int(input("Enter age: "))
    if age >= 18:
        count += 1

print("Eligible people:", count)