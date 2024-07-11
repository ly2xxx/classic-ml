class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

print("[Class variable]")
print(Dog.species)  # Accessing class variable
print(dog1.species)  # Also accessing class variable
print(dog2.species)  # Also accessing class variable

print("""[Instance variable]
    ...
      """)
print(dog1.name)  # Accessing instance variable
print(dog2.name)  # Accessing instance variable

print("""[Modify class variable]
    ...
      """)
Dog.species = "Canis lupus familiaris"  # Modifying class variable
print(dog1.species)  # All instances reflect the change

print("""[Modify instance variable]
    ...
      """)
dog1.species = "Changed"  # This creates a new instance variable for dog1
print(Dog.species)  # Class variable remains unchanged
print(dog2.species)  # Other instances still use the class variable
print(dog1.species)  # dog1 now has its own instance variable 'species'