# class attribute is defined once and it lives
# on the class itself, so directly on the class,
# and they're shared. So whatever class attributes
# we define are shared by all instances, they
# kind of all point to the same class attribute.

class Pet:
    # class attribute that prevent other pets
    # to be called. Only pets that are allowed
    # are in the list.
    allowed = ['cat','dog','fish','horse']
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
    
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
# bear = Pet("Rolly", "bear")

print(cat.name, cat.species)
print(dog.name, dog.species)
# print(bear.name, bear.species)
print(cat.set_species("lion"))