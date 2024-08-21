# 1. Define a static variable and access that through a class
class ExampleClass:
    static_variable = 10  # Static variable defined at the class level

# Accessing the static variable through the class
print("Accessing through class:", ExampleClass.static_variable)

# 2. Define a static variable and access that through an instance
instance = ExampleClass()  # Creating an instance of the class

# Accessing the static variable through the instance
print("Accessing through instance:", instance.static_variable)

# 3. Define a static variable and change within the instance
instance.static_variable = 20  # Attempting to change the static variable through the instance

# Checking the value after modification
print("After modifying through instance:")
print("Accessing through instance:", instance.static_variable)
print("Accessing through class:", ExampleClass.static_variable)

# 4. Define a static variable and change within the class
ExampleClass.static_variable = 30  # Changing the static variable through the class

# Checking the value after modification
print("After modifying through class:")
print("Accessing through class:", ExampleClass.static_variable)
print("Accessing through instance:", instance.static_variable)
