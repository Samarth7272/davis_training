# Question 19: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list


N = int(input("Enter N: "))

print(f"Even numbers between 1 and {N}:")
print(*[i for i in range(2, N+1, 2)])