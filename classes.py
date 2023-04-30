class Member:
    # Class Attributes
    welcome_message = "Welcome"

    def __init__(self, first_name, middle_name, last_name):
        # Instance Attributes
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.welcome_message} {self.first_name} {self.middle_name} {self.last_name}"


member_one = Member("Ahmed", "Seif", "Elnasr")
print(member_one.full_name())
