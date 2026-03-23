# Question 5: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest:", simple_interest(p, r, t))


