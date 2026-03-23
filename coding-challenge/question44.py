# Question 44: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list


N = int(input("Enter N: "))

print(f"Even numbers between 1 and {N}:")
evens = [i for i in range(1, N+1) if i % 2 == 0]

for num in evens:
    print(num, end=" ")