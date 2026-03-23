# Question 30: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest

def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100        

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))    
simple_interest = calculate_simple_interest(p, r, t)
print("Simple Interest:", simple_interest)