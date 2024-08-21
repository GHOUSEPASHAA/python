# 1. Write a function for arithmetic operators (+, -, *, /)

def arithmetic_operations(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")

arithmetic_operations(10, 5)


# 2. Write a method for increment and decrement operators (++, --)

def increment_decrement_operations(x):
    x += 1  # Increment (Python doesn't have ++ operator)
    print(f"After Increment: {x}")
    x -= 1  # Decrement (Python doesn't have -- operator)
    print(f"After Decrement: {x}")

increment_decrement_operations(10)


# 3. Write a program to find if two numbers are equal or not.

def check_equality(num1, num2):
    if num1 == num2:
        print(f"{num1} and {num2} are equal.")
    else:
        print(f"{num1} and {num2} are not equal.")

check_equality(10, 20)
check_equality(15, 15)


# 4. Program for relational operators (<, <=, >, >=)

def relational_operations(a, b):
    print(f"{a} < {b}: {a < b}")
    print(f"{a} <= {b}: {a <= b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} >= {b}: {a >= b}")

relational_operations(10, 20)
relational_operations(30, 20)


# 5. Print the smaller and larger number

def find_smaller_larger(x, y):
    smaller = min(x, y)
    larger = max(x, y)
    print(f"Smaller number is: {smaller}")
    print(f"Larger number is: {larger}")

find_smaller_larger(15, 25)
