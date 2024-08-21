# 1. Create a class with PRIVATE fields, private method and a main method
# Print the fields in main method. Call the private method in main method.
class A:
    def __init__(self):
        self.__private_field = "Private Field in A"  # Private field
        self.protected_field = "Protected Field in A"  # Protected field (conventionally)
        self.public_field = "Public Field in A"  # Public field

    # Private method
    def __private_method(self):
        print("Private method in A")

    # Public method
    def public_method(self):
        print("Public method in A")

    def main(self):
        # Print private field and call private method
        # Direct access to private field and method is not allowed outside the class
        # So, we use a public method to access private members
        print(f"Accessing private field from main: {self.__private_field}")
        self.__private_method()
        # Call public method
        self.public_method()

# Create an instance of A and call the main method
obj_a = A()
obj_a.main()

# Trying to access private fields and methods from subclass
class B(A):
    def __init__(self):
        super().__init__()

    def access_private_from_subclass(self):
        try:
            print(self.__private_field)  # Attempt to access private field
        except AttributeError:
            print("Cannot access private field from subclass")
        
        try:
            self.__private_method()  # Attempt to call private method
        except AttributeError:
            print("Cannot call private method from subclass")

# Create an instance of B and try to access private fields and methods
obj_b = B()
obj_b.access_private_from_subclass()

# 2. Create a class with PROTECTED fields and methods. Access these fields and methods
# from any other class in the same package and from a child class located in a different package
# Protected fields and methods (conventionally)
class C:
    def __init__(self):
        self._protected_field = "Protected Field in C"
    
    def _protected_method(self):
        print("Protected method in C")

# Create an instance of C and access protected fields and methods
obj_c = C()
print(f"Accessing protected field from same package: {obj_c._protected_field}")
obj_c._protected_method()

# Access protected fields and methods from subclass in a different package
class D(C):
    def __init__(self):
        super().__init__()

    def access_protected_from_subclass(self):
        print(f"Accessing protected field from subclass: {self._protected_field}")
        self._protected_method()

# Create an instance of D and access protected fields and methods
obj_d = D()
obj_d.access_protected_from_subclass()

# Access protected fields and methods from a class in a different package
class E:
    def __init__(self):
        self._protected_field = "Protected Field in E"
    
    def _protected_method(self):
        print("Protected method in E")

    def access_protected(self, obj):
        # Access protected fields and methods from an instance of another class
        try:
            print(f"Accessing protected field from another class: {obj._protected_field}")
            obj._protected_method()
        except AttributeError:
            print("Cannot access protected members from another class")

# Create an instance of E and access protected fields and methods
obj_e = E()
obj_e.access_protected(obj_c)  # Passing obj_c to access its protected members

# 3. Create a class with PUBLIC fields and methods. Access the public methods and fields
# from any class in the same package or different package
class F:
    def __init__(self):
        self.public_field = "Public Field in F"
    
    def public_method(self):
        print("Public method in F")

# Create an instance of F and access public fields and methods
obj_f = F()
print(f"Accessing public field from same/different package: {obj_f.public_field}")
obj_f.public_method()

# This code should be in a separate file or module if demonstrating different packages.
# For the sake of this example, we assume that all code is in the same file.

# Demonstrate access from a different package (not actually different packages in this code but would be in practice)
class G:
    def __init__(self):
        self.public_field = "Public Field in G"
    
    def public_method(self):
        print("Public method in G")

# Create an instance of G and access public fields and methods
obj_g = G()
print(f"Accessing public field from different package: {obj_g.public_field}")
obj_g.public_method()
