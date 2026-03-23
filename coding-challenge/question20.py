# Question 20: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest

n = int(input("Enter number of cases: "))
total_si = 0

for i in range(n):
    p = float(input("Enter P: "))
    r = float(input("Enter R: "))
    t = float(input("Enter T: "))

    si = (p * r * t) / 100
    total_si += si

print("Total Simple Interest:", total_si)