# Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def maximum(x, y):
    return x if x > y else y

def minimum(x, y):
    return x if x < y else y

def average(x, y):
    return (x + y) / 2

def is_equal(x, y):
    return x == y

