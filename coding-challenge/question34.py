# Question 34: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list


N = int(input("Enter the value of N: "))
# Print all even numbers between 1 to N
print(f"Even numbers between 1 and {N}:")
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i, end=' ')