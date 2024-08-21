# Define the superclass A
class A:
    def __init__(self):
        self.data = "A's data"
    
    # Method specific to class A
    def method_a1(self):
        print("Method A1 from class A")

    # Method specific to class A
    def method_a2(self):
        print("Method A2 from class A")
    
    # Overridden method
    def overridden_method(self):
        print("Overridden method in class A")

# Define the subclass B, which inherits from A
class B(A):
    def __init__(self):
        super().__init__()
        self.data = "B's data"
    
    # Method specific to class B
    def method_b1(self):
        print("Method B1 from class B")

    # Method specific to class B
    def method_b2(self):
        print("Method B2 from class B")

    # Overridden method
    def overridden_method(self):
        print("Overridden method in class B")

# Define the subclass C, which inherits from B
class C(B):
    def __init__(self):
        super().__init__()
        self.data = "C's data"
    
    # Method specific to class C
    def method_c1(self):
        print("Method C1 from class C")

    # Method specific to class C
    def method_c2(self):
        print("Method C2 from class C")
    
    # Overridden method
    def overridden_method(self):
        print("Overridden method in class C")

# Main class with the main method
class MainClass:
    def main(self):
        # Create instances of A, B, and C
        obj_a = A()
        obj_b = B()
        obj_c = C()

        # Call methods from class A
        print("\nCalling methods from class A:")
        obj_a.method_a1()
        obj_a.method_a2()
        obj_a.overridden_method()

        # Call methods from class B
        print("\nCalling methods from class B:")
        obj_b.method_a1()  # Inherited from A
        obj_b.method_a2()  # Inherited from A
        obj_b.method_b1()
        obj_b.method_b2()
        obj_b.overridden_method()

        # Call methods from class C
        print("\nCalling methods from class C:")
        obj_c.method_a1()  # Inherited from A
        obj_c.method_a2()  # Inherited from A
        obj_c.method_b1()  # Inherited from B
        obj_c.method_b2()  # Inherited from B
        obj_c.method_c1()
        obj_c.method_c2()
        obj_c.overridden_method()

        # Call overridden methods with superclass references
        print("\nCalling overridden methods with superclass references:")
        a_ref = obj_b
        a_ref.overridden_method()  # Calls B's overridden method

        a_ref = obj_c
        a_ref.overridden_method()  # Calls C's overridden method

        # Show runtime polymorphism with data members
        print("\nData members with runtime polymorphism:")
        print("Data in obj_a:", obj_a.data)
        print("Data in obj_b:", obj_b.data)
        print("Data in obj_c:", obj_c.data)

# Instantiate MainClass and run the main method
main_class = MainClass()
main_class.main()
