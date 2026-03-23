# Question 9: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list

n = int(input("Enter N: "))

for i in range(2, n + 1, 2):
    print(i, end=" ")