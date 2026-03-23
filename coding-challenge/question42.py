# Question 42: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible

while True:
    age = int(input())

    if age == -1:
        break

    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")