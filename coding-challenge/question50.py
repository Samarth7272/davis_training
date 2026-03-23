# Question 50: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest


def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

float_p = float(input("Enter Principal (P): "))
if float_p <= 0:
    print("Principal must be greater than 0.")
else:
    float_r = float(input("Enter Rate of Interest (R): "))
    if float_r <= 0:
        print("Rate of Interest must be greater than 0.")
    else:
        float_t = float(input("Enter Time (T) in years: "))
        if float_t <= 0:
            print("Time must be greater than 0.")
        else:
            simple_interest = calculate_simple_interest(float_p, float_r, float_t)
            print(f"Simple Interest: {simple_interest:.2f}")