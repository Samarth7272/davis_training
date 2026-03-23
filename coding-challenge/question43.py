
# Question 43: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount


n = int(input("Enter number of entries: "))
total = 0

for i in range(n):
    u = int(input("Enter units consumed: "))

    if u <= 100:
        bill = u * 5
    elif u <= 200:
        bill = u * 7
    else:
        bill = u * 10

    total += bill

print(total)