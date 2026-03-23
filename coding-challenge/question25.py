# Question 25: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest



p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

si = lambda p, r, t: (p*r*t)/100

print(f"Simple Interest: {si(p,r,t)}")