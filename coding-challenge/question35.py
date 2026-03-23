# Question 35: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest

n = int(input())
total = 0

for i in range(n):
    p = float(input())
    r = float(input())
    t = float(input())

    total += (p * r * t) / 100

print("Average SI:", total / n)