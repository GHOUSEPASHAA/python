from abc import ABC, abstractmethod

# 1. Create an abstract class with abstract and non-abstract methods
class AbstractClass(ABC):
    def __init__(self):
        self.data = "Data in AbstractClass"

    @abstractmethod
    def abstract_method(self):
        """Abstract method that must be implemented by subclasses"""
        pass

    def non_abstract_method(self):
        """Non-abstract method"""
        print("Non-abstract method in AbstractClass")

# 2. Create a subclass for the abstract class. Create an object in the child class
# for the abstract class and access the non-abstract methods
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        """Implementation of the abstract method"""
        print("Abstract method implemented in ConcreteClass")

    def call_methods(self):
        """Calls methods from AbstractClass"""
        self.non_abstract_method()

# Create an instance of ConcreteClass and call non-abstract methods
obj_concrete = ConcreteClass()
print("Calling non-abstract method from ConcreteClass instance:")
obj_concrete.call_methods()

# 3. Create an instance for the child class in child class and call abstract methods
class AnotherConcreteClass(AbstractClass):
    def abstract_method(self):
        """Implementation of the abstract method"""
        print("Abstract method implemented in AnotherConcreteClass")

    def create_instance_and_call_abstract(self):
        """Creates an instance of ConcreteClass and calls abstract methods"""
        instance = ConcreteClass()  # Creating an instance of ConcreteClass
        instance.abstract_method()  # Calling abstract method
        return instance

# Create an instance of AnotherConcreteClass and call abstract methods
obj_another_concrete = AnotherConcreteClass()
print("Calling abstract method through AnotherConcreteClass instance:")
instance_concrete = obj_another_concrete.create_instance_and_call_abstract()

# 4. Create an instance for the child class in child class and call non-abstract methods
class YetAnotherConcreteClass(AbstractClass):
    def abstract_method(self):
        """Implementation of the abstract method"""
        print("Abstract method implemented in YetAnotherConcreteClass")

    def create_instance_and_call_non_abstract(self):
        """Creates an instance of ConcreteClass and calls non-abstract methods"""
        instance = ConcreteClass()  # Creating an instance of ConcreteClass
        instance.non_abstract_method()  # Calling non-abstract method

# Create an instance of YetAnotherConcreteClass and call non-abstract methods
obj_yet_another_concrete = YetAnotherConcreteClass()
print("Calling non-abstract method through YetAnotherConcreteClass instance:")
obj_yet_another_concrete.create_instance_and_call_non_abstract()
