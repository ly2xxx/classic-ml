class MyClass:
    class_attribute = "I'm a class attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    def instance_method(self):
        print(f"Instance method called. Instance attribute: {self.instance_attribute}")
        print(f"Class attribute: {self.class_attribute}")

    @classmethod
    def class_method(cls):
        print(f"Class method called. Class attribute: {cls.class_attribute}")
        # Can't access instance_attribute here

# Usage
obj = MyClass("I'm an instance attribute")

obj.instance_method()
# Output:
# Instance method called. Instance attribute: I'm an instance attribute
# Class attribute: I'm a class attribute

MyClass.class_method()
# Output:
# Class method called. Class attribute: I'm a class attribute

obj.class_method()  # This also works
# Output:
# Class method called. Class attribute: I'm a class attribute