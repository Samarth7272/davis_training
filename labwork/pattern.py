n = int(input("Enter rows: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print("* " * i)
    else:
        print("# " * i)