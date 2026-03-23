balance = 10000

while True:
    amount = int(input("Enter amount (0 to exit): "))

    if amount == 0:
        break
    elif amount < 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawn successfully. Balance:", balance)