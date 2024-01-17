# The key principle in OOP is the data of 
# polymorphism - an object can take on 
# many(poly) forms(morph).

# the same class method works in a similar
# way for different classes

# Cat.speak() # meow
# Dog.speak() # woof
# Human.speak() # yo

# the same operation workd for different
# kinds of objects

# sample_list = [1,2,3]
# sample_tuple = (1,2,3)
# sample_string = "awesome"
# len(sample_list)
# len(sample_tuple)
# len(sample_string)

class Animal():
    def speak(self):
        raise NotImplemented("Subclass needs to implement this method")
    
class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = Dog()
print(d.speak())
f = Fish()
print(f.speak())