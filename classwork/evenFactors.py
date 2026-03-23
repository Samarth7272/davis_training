# Get input from the user
num = int(input("Enter a number: "))

print(f"Even factors of {num} are:")

# Loop through all numbers from 1 to num
for i in range(1, num + 1):
    if num % i == 0 and i % 2 == 0:  # Check if i is a factor and even
        print(i)