# Base class: Family
class Family:
    def __init__(self, last_name, members, home_address):
        self.last_name = last_name
        self.members = members  # List of family member names
        self.home_address = home_address

    def introduce_family(self):
        return f"The {self.last_name} family lives at {self.home_address} and has {len(self.members)} members."

    def add_member(self, name):
        self.members.append(name)
        print(f"{name} has been added to the {self.last_name} family.")

# Subclass: Parent
class Parent(Family):
    def __init__(self, last_name, members, home_address, job_title):
        super().__init__(last_name, members, home_address)
        self.job_title = job_title

    def introduce_parent(self):
        return f"I am a parent in the {self.last_name} family. My job is {self.job_title}."

# Subclass: Child
class Child(Family):
    def __init__(self, last_name, members, home_address, school_name):
        super().__init__(last_name, members, home_address)
        self.school_name = school_name

    def introduce_child(self):
        return f"I am a child in the {self.last_name} family. I go to {self.school_name}."


# Create an instance of Family
family = Family("Dube", ["Mpho", "Nompie"], "10 Buffalo Street")
print(family.introduce_family())
family.add_member("Baby Oboitshepo")

# Create a Parent instance
parent = Parent("Dube", ["Mpho", "Nompie"], "10 Baffalo Street", "Software Engineer")
print(parent.introduce_parent())

# Create a Child instance
child = Child("Dube", ["Odirile", "Oboitshepo"], "10 Baffalo Street", "Fabulous tots")
print(child.introduce_child())
