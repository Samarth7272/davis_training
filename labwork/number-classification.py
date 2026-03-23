def classify(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    if num != 0:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")


n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    classify(num)