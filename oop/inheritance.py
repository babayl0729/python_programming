# a key of OOP is the ability to define a 
# class which inherits from another class
# (a "base" or "parent" class).
# in Python, inheritance works by passing
# the parent class an argument to the 
# definition of a child class:

class Animal:
    cool =  True

    def make_sound(self,sound):
        print(f"this animal says {sound}")

# there is nothing in Cat
# so you need to add "pass"
# otherwise it'll give you
# an error "expected indented block".
class Cat(Animal):
    pass 

blue = Cat()
blue.make_sound("MEOW")
print(blue.cool)
print(Cat.cool)
print(Animal.cool)

# isinstance() is to verify that blue is a Cat
# and blue is also Animal.
print(isinstance(blue, object))
