# Question 40: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest


def si(p,r,t):
    return (p*r*t)/100

print(si(float(input()), float(input()), float(input())))