# super() refers to base calss, parent class
# or whatever the current class is.
# in super() you don't have to specify self
# it'll automatically passed in.
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"
    
    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    def __init__(self,name,breed,toy):
        super().__init__(name,species="Cat")
        self.breed = breed
        self.toy = toy
    
    def play(self):
        print(f"{self.name} plays with {self.toy}")
    
    def kind(self):
        print(f"this {self.species}'s breed is {self.breed}")


blue = Cat("Blue","Scottish Fold","String")
print(blue.__repr__())
blue.play()
blue.make_sound("MEOW!")
blue.kind()




