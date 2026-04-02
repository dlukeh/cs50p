class Package:
    # 1. The constructor (__init__)
    # 2. This runs the moment you "create" a package
    def __init__(self, item, weight):
        self.item = item  # Instance Variable
        self.weight = weight  # Instance Variable

    # 2. A Method
    # This ia a function that belongs to the package
    def calculate_shipping(self):
        return self.weight * 0.50  # Shipping cost is $0.50 per kg

    # 3. A Magic Method
    # This defines what happens when you print (package)

    def __str__(self):
        return f"A {self.item} weighing {self.weight} kg"


# --- Using the Class ---

# 4. Creating an instances (Objects)
package1 = Package("laptop", 2.5)
package2 = Package("keyboard", 0.5)

print(package1)  # This will call the __str__ method
print(f"Shipping cost for {package1.item}: ${package1.calculate_shipping():.2f}")
