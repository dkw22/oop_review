# OOP Shopping cart:
# object -> cart (lists or dictionaries)
# attributes -> items or items, price, quantity,
# behaviors -> add items, remove items, see the items, clear the cart completely, quit

# object oriented programing, aka OOP
# basis of oop is an object
# objects have characteristics:
# attributes and behaviors
# focuses on making reusable code
# DRY = Dont Repeat Yourself
# example of an object:
# cat would be object, a cat can have the following properties:
# name, age, color, weight, breed -> attributes (decribing what the object is like)
# talk, sing, play, sleep, eat, jump -> behaviors (what actions the object can do)
# Basic Principles:
# Object
# Classes
# Methods
# Interitance
# Objects:
#object = instance
# object is instantiation of a class
# an instance is a specific object from a particular class
# Classes:
# blueprint for an object you want to create
# Class is a sketch of our cat object, with labels
# labels contain attributes and behaviors
# when a class is defined, its only the description of the object, the object itself is not actually defined yet
# in order to define (or make) our object, that will be where we instantiate our class
# Class Syntax:
class Cat():
    # attributes: name, age, color, weight, species
    # class attribute (these should stay the same, no matter how many instances we create)
    species = "cat"
    # instance attributes (these change with each instance of the class)

    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    # making methods for our behaviors
    #behaviors: talking and singing

    def talking(self):
        print(f"{self.name} is now talking to itself in the corner.")

    def singing(self, song):
        print(f"{self.name} can sing the song: {song}")


cat1 = Cat("Hecate", 5, "Black", "30lbs")
cat2 = Cat("Tate", 2, "orange", "80lbs")

# accessing class attributes
# print(f"This animal class is based on the {cat1.__class__.species} species.")
# print(f"This animal class is based on the {cat2.__class__.species} species.")

# accessing instance attributes
# print(f"{cat1.name} is {cat1.age} years old and weighs {cat1.weight}.")
# print(f"{cat2.name} is {cat2.age} years old and weighs {cat2.weight}.")

# calling instance methods:
cat1.talking()
cat2.singing("Happy Birthday")

# Interitance:
# just a way to create a new class that use details of an exsiting class, w/o modifying that existing class
# new class is a derived class aka child class
# old class is a base class aka parent class
# we want to make a class of Maine Coon


class MaineCoon(Cat):
    def __init__(self):
        # super allows us to run the init method of the PARENT class
        super().__init__("cat", 3, "orange", "50lbs")

    def talking(self):
        print(f"{self.name} is now talking to its parent.")

    def singing(self, song):
        print(f"{self.name} can sing the song: {song}")

    def sleeping(self):
        print(f"{self.name} is currently sleeping.")


garfield = MaineCoon()
garfield.talking()
garfield.sleeping()
garfield.singing("Twinkle Twinkle Little Star")
