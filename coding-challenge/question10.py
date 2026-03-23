# Question 10: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest

count = int(input("How many calculations: "))

for i in range(count):
    print("\nCalculation", i + 1)

    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate: "))
    t = float(input("Enter Time: "))

    si = (p * r * t) / 100
    print("Simple Interest:", si)