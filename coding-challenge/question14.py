# Question 14: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list

n = int(input("Enter N: "))
even_list = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even_list.append(i)

print("Even Numbers:", even_list)