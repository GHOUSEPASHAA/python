# 1. Write a class with a default constructor, one argument constructor and two argument constructors
class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            # Default constructor
            self.value1 = "Default"
            self.value2 = "Default"
            print("Default constructor called")
        elif arg2 is None:
            # One argument constructor
            self.value1 = arg1
            self.value2 = "Default"
            print(f"One argument constructor called with arg1={arg1}")
        else:
            # Two argument constructor
            self.value1 = arg1
            self.value2 = arg2
            print(f"Two argument constructor called with arg1={arg1} and arg2={arg2}")

# Main class to instantiate MyClass and call all constructors
class MainClass:
    def __init__(self):
        print("Creating instance of MyClass with default constructor:")
        self.obj1 = MyClass()  # Calls default constructor
        
        print("\nCreating instance of MyClass with one argument constructor:")
        self.obj2 = MyClass("Value1")  # Calls one argument constructor
        
        print("\nCreating instance of MyClass with two argument constructor:")
        self.obj3 = MyClass("Value1", "Value2")  # Calls two argument constructor

# Create an instance of MainClass
main = MainClass()

# 2. Call the constructors (both default and argument constructors) of super class from a child class
class Parent:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Parent class default constructor called")
        elif arg2 is None:
            print(f"Parent class one argument constructor called with arg1={arg1}")
        else:
            print(f"Parent class two argument constructor called with arg1={arg1} and arg2={arg2}")

class Child(Parent):
    def __init__(self, arg1=None, arg2=None):
        # Calling constructors of the parent class
        if arg1 is None and arg2 is None:
            super().__init__()  # Calls default constructor of Parent
        elif arg2 is None:
            super().__init__(arg1)  # Calls one argument constructor of Parent
        else:
            super().__init__(arg1, arg2)  # Calls two argument constructor of Parent

        print("Child class constructor called")

# Create instances of Child class
print("\nCreating instance of Child with default constructor:")
child1 = Child()  # Calls Parent default constructor

print("\nCreating instance of Child with one argument constructor:")
child2 = Child("ChildValue1")  # Calls Parent one argument constructor

print("\nCreating instance of Child with two argument constructor:")
child3 = Child("ChildValue1", "ChildValue2")  # Calls Parent two argument constructor

# 3. Apply private, public, protected, and default access modifiers to the constructor
class AccessModifiers:
    def __init__(self):
        # Public constructor
        self.public_value = "Public Value"
        # Protected constructor
        self._protected_value = "Protected Value"
        # Private constructor
        self.__private_value = "Private Value"

    # Public method
    def public_method(self):
        print("Public method accessing private and protected values:")
        print(f"Private Value: {self.__private_value}")
        print(f"Protected Value: {self._protected_value}")
        print(f"Public Value: {self.public_value}")

# 4. Write a program which illustrates the concept of attributes of a constructor
class ConstructorAttributes:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Constructor called with name={name} and age={age}")

    def show_attributes(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create instances and demonstrate constructor attributes
print("\nDemonstrating constructor attributes:")
attributes = ConstructorAttributes("Alice", 30)
attributes.show_attributes()

print("\nDemonstrating access modifiers:")
access_modifiers = AccessModifiers()
access_modifiers.public_method()

