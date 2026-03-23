def is_palindrome(s):
    return s == s[::-1]

val = input("Enter value: ")

if is_palindrome(val):
    print("Palindrome")
else:
    print("Not Palindrome")