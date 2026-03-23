# Question 37: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible

n = int(input())
min_age = 1000

for i in range(n):
    age = int(input())
    if age >= 18 and age < min_age:
        min_age = age

if min_age == 1000:
    print("No eligible person")
else:
    print(min_age)