# Question 49: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list

N = int(input("Enter N: "))
i = 2

print(f"Even numbers between 1 and {N}:")
while i <= N:
    print(i, end=" ")
    i += 2