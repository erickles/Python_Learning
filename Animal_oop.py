class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

my_animal = Animal()

my_animal.who_am_i()
my_animal.eat()

# Inheritance
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I am a dog and I am eating")

    def bark(self):
        print("Woof!")

my_dog = Dog()

my_dog.who_am_i()
my_dog.eat()
my_dog.bark()