# 1. Write a program to print “Bright IT Career” ten times using for loop
for _ in range(10):
    print("Bright IT Career")

# 2. Write a Python program to print 1 to 20 numbers using the while loop.
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1
print()

# 3. Program to demonstrate equal (==) and not equal (!=) operators
a = 10
b = 20
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# 4. Write a program to print the odd and even numbers from 1 to 10.
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# 5. Write a program to print the largest number among three numbers.
num1, num2, num3 = 10, 20, 15
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is", largest)

# 6. Write a program to print even numbers between 10 and 20 using a while loop.
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

# 7. Write a program to print 1 to 10 using the do-while loop statement (emulated using a while loop).
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 10:
        break
print()

# 8. Write a program to find if a number is an Armstrong number or not.
num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# 9. Write a program to find if a number is prime or not.
num = 29
if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# 10. Write a program to check if a number is a palindrome or not.
num = 121
temp = num
reverse_num = 0
while temp > 0:
    digit = temp % 10
    reverse_num = reverse_num * 10 + digit
    temp //= 10
if num == reverse_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")

# 11. Program to check whether a number is EVEN or ODD using switch (emulated using a dictionary in Python)
def check_even_odd(num):
    switcher = {
        0: "Even",
        1: "Odd"
    }
    return switcher.get(num % 2, "Invalid input")

num = 7
print(f"{num} is {check_even_odd(num)}")

# 12. Print gender (Male/Female) program according to given M/F using switch (emulated using a dictionary in Python)
def gender_check(char):
    switcher = {
        'M': "Male",
        'F': "Female"
    }
    return switcher.get(char.upper(), "Invalid input")

gender = 'F'
print(f"The gender is {gender_check(gender)}")
