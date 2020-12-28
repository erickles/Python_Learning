class Dog():

    # Class object attribute
    # Same for any instance of a class
    species = 'mammal'
    
    def __init__(self,breed,name,spots):

        # Attributes
        #  We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

    # Operations/Actions ---> Methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}!".format(self.name, number))

my_dog = Dog(breed='Vira Lata', name='Jujuba',spots=True)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)

my_dog.bark(1)