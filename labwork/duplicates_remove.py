
arr = [1, 5, 3, 5, 7, 5, 9, 2, 5, 8, 6, 5, 4, 5, 0]

num = int(input("Enter a number: "))


if num in arr:
    first_index = arr.index(num)  

    count = arr.count(num)

    for i in range(count - 1):
        arr.remove(num)

    arr.insert(first_index, num)

else:
    print("Number not found in list")

print("Updated list:", arr)