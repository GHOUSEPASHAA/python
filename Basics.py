# 1. Write a program to print your name.
print("Mohiuddin Ghouse Pasha")

# 2. Write a program for a Single line comment and multi-line comments

# This is a single-line comment

"""
This is a 
multi-line comment
"""

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

# Integer
int_var = 10
print("Integer:", int_var)

# Boolean
bool_var = True
print("Boolean:", bool_var)

# Character (Python does not have a separate char data type; we use strings of length 1)
char_var = 'A'
print("Character:", char_var)

# Float
float_var = 10.5
print("Float:", float_var)

# Double (Python's float is equivalent to double in other languages)
double_var = 20.123456789
print("Double:", double_var)

# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables

global_var = "I am a global variable"

def my_function():
    global global_var
    local_var = "I am a local variable"
    global_var = "I am modified global variable inside the function"
    print("Inside function - Local variable:", local_var)
    print("Inside function - Global variable:", global_var)

my_function()

print("Outside function - Global variable:", global_var)
