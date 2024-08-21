# 1. Write a program to generate Arithmetic Exception without exception handling
def generate_arithmetic_exception():
    print("Generating Arithmetic Exception without handling:")
    # Division by zero to generate ArithmeticError
    result = 1 / 0

# 2. Handle the Arithmetic Exception using try-catch block
def handle_arithmetic_exception():
    print("\nHandling Arithmetic Exception with try-except block:")
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"Handled Arithmetic Exception: {e}")

# 3. Write a method which throws exception, Call that method in main class without try block
def method_throwing_exception():
    print("\nMethod that throws an exception:")
    raise ValueError("This is a custom exception thrown from a method.")

def call_method_without_try():
    print("\nCalling method without try block:")
    method_throwing_exception()

# 4. Write a program with multiple catch blocks
def multiple_catch_blocks():
    print("\nHandling multiple exceptions with try-except blocks:")
    try:
        # Generate different exceptions
        value = int("string")  # Will raise ValueError
        result = 1 / 0         # Will raise ZeroDivisionError
    except ValueError as e:
        print(f"ValueError caught: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")

# 5. Write a program to throw exception with your own message
def throw_exception_with_message():
    print("\nThrowing exception with a custom message:")
    raise RuntimeError("This is a custom exception with a message.")

# 6. Write a program to create your own exception
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CustomException: {self.message}"

def use_custom_exception():
    print("\nUsing a custom exception:")
    raise CustomException("This is a custom exception message.")

# 7. Write a program with finally block
def finally_block_example():
    print("\nUsing finally block:")
    try:
        print("Inside try block")
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"Handled exception: {e}")
    finally:
        print("This will always execute, regardless of an exception")

# 8. Write a program to generate Arithmetic Exception
def generate_arithmetic_exception_again():
    print("\nGenerating Arithmetic Exception again:")
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"Handled Arithmetic Exception: {e}")

# 9. Write a program to generate FileNotFoundException
def generate_file_not_found_exception():
    print("\nGenerating FileNotFoundException:")
    try:
        with open("non_existent_file.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"FileNotFoundError caught: {e}")

# 10. Write a program to generate ClassNotFoundException
def generate_class_not_found_exception():
    print("\nGenerating ClassNotFoundException:")
    try:
        # Simulate class not found by trying to import a non-existent module
        import non_existent_module
    except ImportError as e:
        print(f"ImportError caught: {e}")

# 11. Write a program to generate IOException
def generate_io_exception():
    print("\nGenerating IOException:")
    try:
        with open("example.txt", 'w') as file:
            # Simulate IOError by closing the file and then attempting to write
            file.write("Some text")
            file.close()
            file.write("More text")  # This will raise an IOError
    except IOError as e:
        print(f"IOError caught: {e}")

# 12. Write a program to generate NoSuchFieldException
def generate_no_such_field_exception():
    print("\nGenerating NoSuchFieldException:")
    try:
        class ExampleClass:
            def __init__(self):
                self.existing_field = 42

        obj = ExampleClass()
        # Simulate accessing a non-existent attribute
        value = getattr(obj, 'non_existent_field')
    except AttributeError as e:
        print(f"AttributeError caught: {e}")

# Main program to execute all functions
if __name__ == "__main__":
    generate_arithmetic_exception()
    handle_arithmetic_exception()
    call_method_without_try()
    multiple_catch_blocks()
    throw_exception_with_message()
    use_custom_exception()
    finally_block_example()
    generate_arithmetic_exception_again()
    generate_file_not_found_exception()
    generate_class_not_found_exception()
    generate_io_exception()
    generate_no_such_field_exception()
