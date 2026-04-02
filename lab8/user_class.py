class User:
    def __init__(self, name):
        self.name = name  # The data lives here

    # This is a Method because it's inside the class
    def greet(self):
        return f"Hello, I am {self.name}!"  # This is a string interpolation, it will replace {self.name} with the value of self.name


# You create the object
my_user = User("Nyra")

# You call the method ON the object
print(my_user.greet())  # This will print "Hello, I am Nyra!"
