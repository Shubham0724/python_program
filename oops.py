#Creating a Class:
class Details:
    name = "Central"
    age = 20

#Creating an Object:
class Details:
    name = "Central"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)    

#self method
class Details:
    name = "Central"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()

#__init__ method
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")