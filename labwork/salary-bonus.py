def bonus(salary, years):
    if years >= 10:
        return salary * 0.20
    elif years >= 5:
        return salary * 0.10
    else:
        return salary * 0.05

for i in range(3):
    salary = int(input("Enter salary: "))
    years = int(input("Enter experience: "))
    print("Bonus:", bonus(salary, years))