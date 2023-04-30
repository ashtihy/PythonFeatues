class Order:
    def __init__(self, name, order_list):
        self.name = name
        self.order = order_list

    def print_order(self):
        print(self.order)

    # Overloading dunder __str__ method
    def __str__(self):
        return f"{self.name}'s Order is {self.order}"

    # Overloading dunder __class__ method

    @property
    def __class__(self):
        return "Class Name is Order"


order = Order("Ahmed", ["Keyboard", "Mouse"])

# Dunder Attribute which is a dictionary has all class attributes
print(order.__dict__)
print(vars(order))
# __str__ -> Dunder Method which defines what we arg going to print when print(obj_of_class)
print(order)
print(order.__str__())

# __class__ Dunder Method which returns the class name of the object
print(order.__class__)
