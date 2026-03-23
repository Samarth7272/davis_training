# Question 15: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest

def SI(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

print(f"Simple Interest = {SI(p, r, t):.2f}")