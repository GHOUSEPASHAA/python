# 1. Write two methods with the same name but different number of parameters of the same type
class MethodOverloadingSameType:
    def print_message(self, message1, message2=None):
        if message2 is None:
            # Method with one parameter
            print(f"Message: {message1}")
        else:
            # Method with two parameters
            print(f"Message1: {message1}, Message2: {message2}")

# Create an instance and call the methods
print("Calling methods with the same name but different number of parameters (same type):")
obj_same_type = MethodOverloadingSameType()
obj_same_type.print_message("Hello")         # Calls method with one parameter
obj_same_type.print_message("Hello", "World")  # Calls method with two parameters

# 2. Write two methods with the same name but different number of parameters of different data types
class MethodOverloadingDifferentTypes:
    def display(self, value):
        if isinstance(value, str):
            # Method with string parameter
            print(f"String value: {value}")
        elif isinstance(value, int):
            # Method with integer parameter
            print(f"Integer value: {value}")
        else:
            print("Unsupported type")

# Create an instance and call the methods
print("\nCalling methods with the same name but different number of parameters (different types):")
obj_different_types = MethodOverloadingDifferentTypes()
obj_different_types.display("Hello")  # Calls method with string parameter
obj_different_types.display(42)       # Calls method with integer parameter

# 3. Write two methods with the same name and same number of parameters of the same type
class MethodOverloadingSameParameters:
    def calculate(self, x, y):
        result = x + y
        print(f"Sum of {x} and {y} is {result}")

    def calculate(self, x, y):
        result = x * y
        print(f"Product of {x} and {y} is {result}")

# Create an instance and call the methods
print("\nCalling methods with the same name and same number of parameters (same type):")
obj_same_parameters = MethodOverloadingSameParameters()
obj_same_parameters.calculate(5, 3)  # Calls the latest defined 'calculate' method (product)

