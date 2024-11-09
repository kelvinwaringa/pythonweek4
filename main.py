class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, I'm {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# Create an instance of Person
person1 = Person("John Doe", 25, "male")

# Call the introduce method
person1.introduce()