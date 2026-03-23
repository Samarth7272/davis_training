# Question 4: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list

n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")